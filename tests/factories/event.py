"""Event factories for fixtures."""

import factory
from faker import Factory as FakerFactory

from .tech_group import TechGroupFactory

faker = FakerFactory.create()


class EventFactory(factory.django.DjangoModelFactory):
    """Event factory."""

    name = factory.LazyAttribute(lambda x: faker.name())
    tech_group = factory.SubFactory(TechGroupFactory)

    class Meta:  # noqa D201
        model = "data.Event"
