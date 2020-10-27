from django.shortcuts import render
from .models import *
from .serializers import *
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status, mixins, generics
# Create your views here.


class InstituteSignUpView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Institute.objects.all()
    serializer_class = InstituteSignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.validated_data["role"] = "Institute"
        if (
            serializer.validated_data["password2"]
            == serializer.validated_data["password"]
        ):
            serializer.validated_data.pop("password2")
            hashed_password = make_password(
                serializer.validated_data["password"])
            serializer.validated_data["password"] = hashed_password
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"error": "Could not create Institute"}, status=status.HTTP_400_BAD_REQUEST
        )
