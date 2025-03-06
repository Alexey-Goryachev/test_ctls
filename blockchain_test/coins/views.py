from django.shortcuts import render
from django.views import View
from .models import Coin

class CoinListView(View):
    def get(self, request):
        coins = Coin.objects.all()
        return render(request, "coins/index.html", {"coins": coins})

class CoinDetailView(View):
    def get(self, request, ticker):
        coin = Coin.objects.filter(ticker=ticker).first()
        return render(request, "coins/coin_detail.html", {"coin": coin})
