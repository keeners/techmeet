"""Test serializers."""
import pytest

from django.test.client import Client

from rest_framework import status

from data import models
from interface.api import serializers
from tests import factories


@pytest.mark.django_db
def test_get_all_tech_groups(client: Client, tech_group_factory: factories.TechGroupFactory) -> None:
    tech_group_factory(name="One")
    tech_group_factory(name="Two")
    tech_group_factory(name="Three")
    response = client.get("/api/techgroups/")
    tech_groups = models.TechGroup.objects.all()
    serializer = serializers.TechGroupSerializer(tech_groups, many=True)
    response.data == serializer.data
    response.status_code == status.HTTP_200_OK
