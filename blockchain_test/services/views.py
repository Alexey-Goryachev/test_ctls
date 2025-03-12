from asgiref.sync import async_to_sync
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from coins.karbo.client import KarboClient
from coins.polygon.client import PolygonClient
from coins.usdt_polygon.client import USDTPolygonClient
from coins.tron.client import TronClient
from coins.serializers import BalanceSerializer

# Create your views here.
karbo_client = KarboClient()
polygon_client = PolygonClient()
usdt_client = USDTPolygonClient()
tron_client = TronClient()

CLIENTS = {
    "KRB": karbo_client,
    "POL": polygon_client,
    "USDT_P": usdt_client,
    "TRX": tron_client,
}

class GetBlockView(APIView):
    def get(self, request, ticker: str) -> Response:
        try:
            client = CLIENTS.get(ticker.upper())
            if not client:
                return Response({"error": "Unknown coin"}, status=status.HTTP_400_BAD_REQUEST)
            
            if isinstance(client, TronClient):
                height = async_to_sync(client.get_height_block)()

            else:
                height = client.get_height_block()

            return Response({"height": height}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)



class BalanceView(APIView):
    def post(self, request, ticker: str) -> Response:
        try:
            client = CLIENTS.get(ticker.upper())
            if not client:
                return Response({"error": "Unknown coin"}, status=status.HTTP_400_BAD_REQUEST)

            serializer = BalanceSerializer(data=request.data, context={"ticker": ticker})
            if serializer.is_valid():
                address = serializer.validated_data["address"]
                if isinstance(client, TronClient):
                    balance = async_to_sync(client.get_balance)(address)
                else:    
                    balance = client.get_balance(address)
                return Response({"balance": balance}, status=status.HTTP_200_OK)
            else:
                print(f"Response: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)


class GetAddressView(APIView):
    def get(self, request, ticker: str) -> Response:
        try:
            client = CLIENTS.get(ticker.upper())
            if not client:
                return Response({"error": "Unknown coin"}, status=status.HTTP_400_BAD_REQUEST)
            
            if isinstance(client, KarboClient):
                address = client.get_address()

            else:
                address = "This functional hasn't unavaibled yet"

            return Response({"address": address}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)
