from django.contrib import admin
from django import forms
from .models import Coin


class CoinAdminForm(forms.ModelForm):
    class Meta:
        model = Coin
        fields = '__all__'

    color_coin = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

class CoinAdmin(admin.ModelAdmin):
    form = CoinAdminForm

admin.site.register(Coin, CoinAdmin)
