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

    async def get_balance(self, address: str) -> Decimal:
        """
        Return balance wallet in TRX unit
        """
        apikey = settings.tron.API_KEY
        client = AsyncTron(AsyncHTTPProvider(api_key=apikey))
        try:
            tron_balance = await client.get_account_balance(addr=address)
            return tron_balance
        except Exception as e:
            raise ValueError(f"Get_balance_tron: {e}")
        
    async def get_address(self) ->str:
        pass
        