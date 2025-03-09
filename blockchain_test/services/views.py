from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from coins.karbo.client import KarboClient
from coins.polygon.client import PolygonClient
from coins.usdt_polygon.client import USDTPolygonClient
from coins.serializers import BalanceSerializer, BlockHeightSerializer

# Create your views here.
karbo_client = KarboClient()
polygon_client = PolygonClient()
usdt_client = USDTPolygonClient()

CLIENTS = {
    "KRB": karbo_client,
    "POL": polygon_client,
    "USDT_P": usdt_client,
}

class GetBlockView(APIView):
    def get(self, request, ticker: str) -> Response:
        client = CLIENTS.get(ticker.upper())
        if not client:
            return Response({"error": "Unknown coin"}, status=status.HTTP_400_BAD_REQUEST)
    
        height = client.get_height_block()
        return Response({"height": height}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BalanceView(APIView):
    def post(self, request, ticker: str) -> Response:
        client = CLIENTS.get(ticker.upper())
        if not client:
            return Response({"error": "Unknown coin"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = BalanceSerializer(data=request.data)
        if serializer.is_valid():
            address = serializer.validated_data["address"]
            balance = client.get_balance(address)
            return Response({"balance": balance}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
