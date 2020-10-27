from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *


class InstituteSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"},
    )

    class Meta:
        model = Institute
        fields = (
            "id",
            "name",
            "email",
            "address",
            "password",
            "password2",
        )
