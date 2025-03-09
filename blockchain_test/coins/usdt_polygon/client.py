from decimal import Decimal
import time

from blockchain_app import setting_coins as settings
from coins.interface import Interface
import requests

__all__ = "USDTPolygonClient"


class USDTPolygonClient(Interface):
    """
    Client for interactive with blockchain Polygon
    """

    def get_height_block(self) -> int:
        """
        Func for get current number block in blockchain
        """
        apikey = settings.usdt_polygon.API_KEY
        timestamp = int(time.time())
        nonerequest = 0
        try:
            while nonerequest == 0:
                time.sleep(1)
                response_block = requests.get(
                    "https://api.polygonscan.com/api?module=block&action=getblocknobytime&timestamp="
                    + str(timestamp)
                    + "&closest=before&apikey="
                    + apikey
                )
                response_block_json = response_block.json()
                if (
                    (str(response_block_json.get("status")) == "1")
                    and (str(response_block_json.get("message")) == "OK")
                    and (str(response_block_json.get("result") != "None"))
                ):
                    polygon_block = int(response_block_json.get("result"))
                    return polygon_block
                else:
                    nonerequest = 0
        except Exception as e:
            raise ValueError(f"Get_height_block_polygon: {e}")

    def get_balance(self, address: str) -> Decimal:
        """
        Return balance wallet in USDT unit on blockchain Polygon
        """
        apikey = settings.usdt_polygon.API_KEY
        contract_address = settings.usdt_polygon.CONTRACT_ADDRESS
        nonerequest = 0
        try:
            while nonerequest == 0:
                time.sleep(1)
                response_balance = requests.get(
                    "https://api.polygonscan.com/api?module=account&action=tokenbalance&contractaddress="
                    + contract_address
                    + "&address="
                    + str(address)
                    + "&tag=latest&apikey="
                    + apikey
                )

                response_balance_json = response_balance.json()

                if (
                    (str(response_balance_json.get("status")) == "1")
                    and (str(response_balance_json.get("message")) == "OK")
                    and (str(response_balance_json.get("result") != "None"))
                ):
                    polygon_balance = int(response_balance_json.get("result"))
                    nonerequest = 1
                else:
                    nonerequest = 0
        except Exception as e:
            raise ValueError(f"Get_balance_polygon: {e}")

        result = Decimal(
            str((float(polygon_balance)) / (10**settings.usdt_polygon.DECIMALS))
        )

        return result