"""Custom user model."""
from typing import Any

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """User manager that uses email as login."""

    def _create_user(
        self, name: str, email: str, password: str, **extra_fields: Any
    ) -> "User":
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_("Email must be set"))
        if not name:
            raise ValueError(_("Name must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(
        self, name: str, email: str, password: str, **extra_fields: Any
    ) -> "User":
        """Create a regular User."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(
        self, name: str, email: str, password: str, **extra_fields: Any
    ) -> "User":
        """Create a super user."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """User model with name and email."""

    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(_("name"), max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    def __str__(self) -> str:
        """Return email as string."""
        return self.email
