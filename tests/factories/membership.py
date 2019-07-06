"""Membership factories for fixtures."""

import factory
from faker import Factory as FakerFactory

from .tech_group import TechGroupFactory
from .user import UserFactory

faker = FakerFactory.create()


class MembershipFactory(factory.django.DjangoModelFactory):
    """Membership factory."""

    user = factory.SubFactory(UserFactory)
    tech_group = factory.SubFactory(TechGroupFactory)

    class Meta:  # noqa D201
        model = "data.Membership"
