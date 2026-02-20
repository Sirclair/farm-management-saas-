from django.db import models
from django.contrib.auth.models import AbstractUser


class Farm(models.Model):
    name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="users")
    role = models.CharField(max_length=20, choices=[
        ("owner", "Owner"),
        ("manager", "Manager"),
        ("staff", "Staff"),
    ], default="staff")