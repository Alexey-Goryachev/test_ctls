from rest_framework import serializers

class BalanceSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=255)

    blockchain_patterns = {
        "KRB": {"prefix": "K", "length": 95},
        "POL": {"prefix": "0x", "length": 42},
        "TRX": {"prefix": "T", "length": 34},
        "USDT_P": {"prefix": "0x", "length": 42},
    }

    blockchain_accounts = {
        "KRB": "https://richamster.com/auth/register?referral=undefined",
        "POL": "https://polygonscan.com/accounts",
        "TRX": "https://tronscan.org/#/blockchain/accounts",
        "USDT_P": "https://polygonscan.com/accounts",
    }

    def validate_address(self, value):
        ticker = self.context.get("ticker", "").upper()
        blockchain = self.blockchain_patterns.get(ticker)

        if not blockchain:
            raise serializers.ValidationError("Unknown blockchain.")

        if not value.startswith(blockchain["prefix"]) or len(value) != blockchain["length"]:
            explorer_url = self.blockchain_accounts.get(ticker, "#")
            raise serializers.ValidationError({
                "message": f"Invalid address format for {ticker}. ",
                "explorer_url": explorer_url
            })

        return value
    