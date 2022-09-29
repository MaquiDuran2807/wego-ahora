from rest_framework import serializers
from .models import account


class AccountSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = account
        fields = (
            'nombre_persona',
            'apellido_persona',
            'cedula_persona',
        )