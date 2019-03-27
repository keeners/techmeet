import factory
from faker import Factory as FakerFactory

faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    """User factory."""

    name = factory.LazyAttribute(lambda x: faker.name())

    class Meta:
        model = 'data.User'

    @factory.lazy_attribute
    def email(self) -> str:
        """Return lower cased name and lets remove spaces."""
        name = self.name.lower().replace(" ", "")
        return f"{name}@example.com"


class SuperUserFactory(UserFactory):
    """Super User factory."""

    is_staff = True
    is_superuser = True
