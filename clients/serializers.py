from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = [
            "id",
            "client_name",
            "cnpj",
            "corporate_name",
            "tel",
            "client_email",
            "contract_health",
            "contract_dental",
            "contract_life",
            "created_at",
            "updated_at",
            "users",
        ]
