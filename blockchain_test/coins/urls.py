from django.urls import path

from . import views

app_name = "coins"

urlpatterns = [
    path('', views.CoinListView.as_view(), name='coin_list'),
    path('<str:ticker>/', views.CoinDetailView.as_view(), name='coin_detail'),
]