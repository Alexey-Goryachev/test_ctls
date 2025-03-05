from django.db import models

# Create your models here.

class Coin(models.Model):

    title = models.CharField(verbose_name="Title", max_length=255, blank=True)

    ticker = models.CharField(verbose_name="Ticker", max_length=10, blank=True)

    explorer = models.URLField(verbose_name="Explorer", max_length=255, blank=True)

    created_at = models.DateTimeField(verbose_name=("Created at"), auto_now_add=True)

    def __str__(self):
        return self.title or self.ticker