"""API Serializers."""
from django.contrib.auth.models import Group, User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User Serializer."""

    class Meta:  # noqa: D106
        model = User
        fields = ("url", "username", "email", "groups")


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Group Serializer."""

    class Meta:  # noqa: D106
        model = Group
        fields = ("url", "name")
