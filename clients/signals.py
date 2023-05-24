from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps
from clients.models import Client
import ipdb

@receiver(post_migrate)
def create_initial_client(sender, **kwargs):
    if not Client.objects.exists():
        client = Client(client_name='FRB', cnpj='1234567890', corporate_name='FRB-Consultoria')
        client.save()