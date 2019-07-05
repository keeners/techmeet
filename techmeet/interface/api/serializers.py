"""API Serializers."""
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import serializers

from data import models

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User Serializer."""

    class Meta:  # noqa: D106
        model = User
        fields = ("id", "url", "email", "name", "date_joined", "groups")


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Group Serializer."""

    class Meta:  # noqa: D106
        model = Group
        fields = ("url", "name")


class TechGroupSerializer(serializers.HyperlinkedModelSerializer):
    """Tech Group serializer."""

    class Meta:  # noqa: D106
        model = models.TechGroup
        fields = ("id", "name", "slug", "description", "logo")
