"""User factories for fixtures."""

import factory
from faker import Factory as FakerFactory

faker = FakerFactory.create()


class TechGroupFactory(factory.django.DjangoModelFactory):
    """TechGroup factory."""

    name = factory.Faker("name")
    description = factory.Faker("description")

    class Meta:  # noqa D201
        model = "data.TechGroup"
