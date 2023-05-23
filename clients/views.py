from rest_framework import generics
from .models import Client
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser



class ClientsView(generics.ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated, IsAdminUser]
    
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientsDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    lookup_url_kwarg = "client_id"