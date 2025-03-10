from decimal import Decimal
import time
import asyncio

from blockchain_app import setting_coins as settings
from coins.interface import Interface
from tronpy import AsyncTron
from tronpy.providers import AsyncHTTPProvider

__all__ = "TronClient"


class TronClient(Interface):
    """
    Client for interactive with blockchain Tron 
    """

    async def get_height_block(self) -> int:
        """
        Func for get current number block in blockchain
        """
        apikey = settings.tron.API_KEY
        client = AsyncTron(AsyncHTTPProvider(api_key=apikey))
        try:
            tron_block = await client.get_latest_block_number()
            return tron_block
        except Exception as e:
            raise ValueError(f"Get_height_block_tron: {e}")

    def get_balance(self, address: str) -> Decimal:
        """
        Return balance wallet in TRX unit
        """
        apikey = settings.polygon.API_KEY
        nonerequest = 0
        try:
            while nonerequest == 0:
                time.sleep(1)
                response_balance = requests.get(
                    "https://api.polygonscan.com/api?module=account&action=balance&address="
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
            str((float(polygon_balance)) / (10**settings.polygon.DECIMALS))
        )

        return result