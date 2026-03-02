from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Farm(models.Model):
    name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    email = models.EmailField()  # removed unique=True (important)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("Users must have a username")

        email = self.normalize_email(email)

        farm_info = extra_fields.pop("farm_info", None)

        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        # Default farm creation
        if farm_info is None:
            farm_info = {
                "name": f"{username}'s Farm",
                "owner_name": username,
                "email": email or "default@example.com",
                "phone": "0000000000",
                "address": "Default Address",
            }

        farm = Farm.objects.create(**farm_info)

        FarmMembership.objects.create(
            user=user,
            farm=farm,
            role="owner"
        )

        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    objects = UserManager()

    def __str__(self):
        return self.username


class FarmMembership(models.Model):
    ROLE_CHOICES = (
        ("owner", "Owner"),
        ("manager", "Manager"),
        ("staff", "Staff"),
        ("accountant", "Accountant"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="farm_memberships"
    )
    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        related_name="memberships"
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "farm")

    def __str__(self):
        return f"{self.user.username} @ {self.farm.name} ({self.role})"