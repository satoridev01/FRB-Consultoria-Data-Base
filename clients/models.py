from django.db import models
import uuid


class Client(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    client_name = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=20)
    corporate_name = models.CharField(max_length=150)
    tel = models.CharField(max_length=20, null=True)
    client_email = models.EmailField(max_length=150, null=True)
    contract_health = models.IntegerField(null=True)
    contract_dental = models.IntegerField(null=True)
    contract_life = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        return f"<Client ({self.id}) - {self.client_name}>"
