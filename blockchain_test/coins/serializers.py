from rest_framework import serializers

class BalanceSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=255)

class BlockHeightSerializer(serializers.Serializer):
    height = serializers.IntegerField()
    