from decimal import Decimal

from blockchain_app import settings
from coins.interface import Interface
from blockchain_app import setting_coins as settings

import requests

__all__ = ("KarboClient")




class KarboClient(Interface):
    '''
    Client for interactive with blockchain Karbo
    '''
    
    def get_height_block(self) -> int:
        '''
        Func for get current number block in blockchain
        '''

        karbo_url = settings.karbo.URL_WALLET

        karbo_block_json = {
            "jsonrpc":"2.0",
            "method":"get_height",
            "params":{}
        }

        command_to_execute = "/json_rpc"
        karbo_get_block_command = karbo_url + command_to_execute

        request_get_block =  requests.post(karbo_get_block_command, json=karbo_block_json)
        karbo_height_block = request_get_block.json().get("result").get("height")

        return karbo_height_block
    

    def get_balance(self, address: str) ->Decimal:
        '''
        Return balance wallet in karbo unit
        '''
        karbo_url = settings.karbo.URL_WALLET

        karbo_balance_json = {
            "jsonrpc":"2.0",
            "method":"get_balance",
            "params":{
                "address": address
            }
        }

        command_to_execute = "/json_rpc"
        karbo_get_block_command = karbo_url + command_to_execute

        request_get_balance =  requests.post(karbo_get_block_command, json=karbo_balance_json)
        karbo_balance_response = request_get_balance.json().get("result").get("available_balance")
        karbo_balance_human = Decimal(karbo_balance_response) /(10 ** settings.karbo.DECIMALS)

        return karbo_balance_human
