
from rest_framework.response import Response
from users.permissions import IsAdminOrReadOnly, IsAdminOrUser
from .models import User
from clients.models import Client
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,  status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
import ipdb


class UsersView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        client_id = self.request.data["client_id"]
        client = get_object_or_404(Client, pk=client_id)
        serializer.save(client=client)

class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"

class SendMailView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.data["username"]).first()
        if(not user.active):
            raise InvalidToken()
        
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
    serializer_class = CustomTokenObtainPairSerializer
