"""API Serializers."""
from django.contrib.auth.models import Group, User

from rest_framework import serializers

from data import models


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


class TechGroupSerializer(serializers.HyperlinkedModelSerializer):
    """Tech Group serializer."""

    class Meta:  # noqa: D106
        model = models.TechGroup
        fields = ("id", "name", "slug", "description", "logo")


class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    """Membership serializer."""

    class Meta:  # noqa D106
        model = models.Membership
        fields = ("id", "tech_group", "user", "date_joined")
