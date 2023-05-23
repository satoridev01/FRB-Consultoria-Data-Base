from rest_framework import generics
from .models import User
from clients.models import Client
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
import ipdb


class UsersView(generics.ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        client_id = self.request.data["client_id"]
        client = get_object_or_404(Client, pk=client_id)
        serializer.save(client=client)


class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"
