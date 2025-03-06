from django.urls import path

from . import views

app_name = "coins"

urlpatterns = [
    path('', views.CoinListView, name='coin_list'),
    path('<str:ticker>/', views.CoinDetailView, name='coin_detail'),
]