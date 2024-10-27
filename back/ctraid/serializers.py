from rest_framework.serializers import ModelSerializer
from .models import Currency


class CurrencyListSerializers(ModelSerializer):
    class Meta:
        model = Currency

        fields = [
            "name",
            "symbol",
            "id"
        ]