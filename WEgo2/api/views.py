from django.shortcuts import render
from .models import account
from .serializers import AccountSerializer

from rest_framework.generics import ListAPIView
# Create your views here.


class AccountList (ListAPIView):
    queryset = account.objects.all()
    serializer_class = AccountSerializer