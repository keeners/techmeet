"""Test serializers."""
from typing import Dict

from django.test.client import Client

import pytest
from rest_framework import status
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from data import models
from interface.api import serializers
from tests import factories


@pytest.fixture
def context() -> Dict:
    """Hyperlinked serializers require a context."""
    factory = APIRequestFactory()
    request = factory.get("/")
    context = {"request": Request(request)}
    return context


@pytest.mark.django_db
def test_get_all_tech_groups(
    client: Client, tech_group_factory: factories.TechGroupFactory
) -> None:
    """Test serializer returns tech groups."""
    tech_group_factory(name="One")
    tech_group_factory(name="Two")
    tech_group_factory(name="Three")
    response = client.get("/api/techgroups/")
    tech_groups = models.TechGroup.objects.all()
    serializer = serializers.TechGroupSerializer(tech_groups, many=True)
    response.data == serializer.data
    response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_all_memberships(
    client: Client, membership_factory: factories.MembershipFactory, context: Dict
) -> None:
    """Test serializer returns memberships."""
    membership_factory()
    membership_factory()
    membership_factory()
    response = client.get("/api/memberships/")
    memberships = models.Membership.objects.all()
    serializer = serializers.MembershipSerializer(
        memberships, many=True, context=context
    )
    response.data == serializer.data
    response.status_code == status.HTTP_200_OK
