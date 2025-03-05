from blockchain_test.blockchain_app import settings

import requests

__all__ = ("KarboClient")




class KarboClient:
    '''Client for interactive with blockchain Karbo'''
    
    def get_height_block(self) -> int:
        '''Func for get current number block in blockchain'''

        karbo_url = settings.krb.URL_WALLET

        karbo_block_json = {
            "jsonrpc":"2.0",
            "method":"get_height",
            "params":{}
        }

        command_to_execute = '/json_rpc'
        karbo_get_block_command = karbo_url + command_to_execute

        request_get_block =  requests.post(karbo_get_block_command, json=karbo_block_json)
        karbo_height_block = request_get_block.json().get('result').get('height')

        return karbo_height_block
    