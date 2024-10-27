from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import Currency
from .serializers import CurrencyListSerializers
from rest_framework import permissions
# Create your views here.


class CurrencyListView(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencyListSerializers
    permission_classes = [permissions.IsAdminUser]
