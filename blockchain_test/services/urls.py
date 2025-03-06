from django.urls import path

from . import views

app_name = "services"

urlpatterns = [
    path('block/<str:ticker>/', views.GetBlockView.as_view(), name='get_block'),
    path('balance/<str:ticker>/', views.BalanceView.as_view(), name='get_balance')
]