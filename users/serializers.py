from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
import ipdb

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        
        if not validated_data["user_level"] == "medic":
            return User.objects.create_user(**validated_data)
        
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "user_level",
            "is_superuser",
            "description",
            "created_at",
            "updated_at",
            "client_id"
        ]

        extra_kwargs = {
            "is_superuser": {"read_only": True},
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that email already exists.",
                    )
                ]
            },
        }