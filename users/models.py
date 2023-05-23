from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(unique=True, max_length=150)
    password = models.CharField(max_length=150)
    description = models.TextField(null=True)
    user_level = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    client = models.ForeignKey(
        "clients.Client",
        related_name="users",
        on_delete=models.CASCADE
    )
    
    def __repr__(self) -> str:
        return f"<User ({self.id}) - {self.username}>"