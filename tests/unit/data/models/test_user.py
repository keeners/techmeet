"""Test User model."""

import pytest

from data import models
from tests import factories


def test_str(user_factory: factories.UserFactory) -> None:
    """Test that the string representation return an email."""
    user = user_factory.build(name="Jane", email="jane@example.com")
    assert str(user) == "jane@example.com"


@pytest.mark.django_db
def test_private_user_create() -> None:
    """Test that we get back an instance of User."""
    user = models.User.objects._create_user("Jane Smith", "hi@me.com", "mypass")
    assert user.name == "Jane Smith"
    assert user.email == "hi@me.com"
    assert user.is_active


@pytest.mark.django_db
def test_private_user_raises_error_when_no_email() -> None:
    """Test that no name raises error."""
    with pytest.raises(ValueError):
        models.User.objects._create_user("Jane Smith", None, "mypass")


@pytest.mark.django_db
def test_private_user_raises_error_when_no_name() -> None:
    """Test that no name raises error."""
    with pytest.raises(ValueError):
        models.User.objects._create_user(None, "hi@me.com", "mypass")


@pytest.mark.django_db
def test_user_create() -> None:
    """Test creation of regular user."""
    user = models.User.objects.create_user("Jane Smith", "hi@me.com", "mypass")
    assert user.name == "Jane Smith"
    assert user.email == "hi@me.com"
    assert user.is_active


@pytest.mark.django_db
def test_superuser_create() -> None:
    """Test creation of regular user."""
    user = models.User.objects.create_superuser("Jane Smith", "hi@me.com", "mypass")
    assert user.name == "Jane Smith"
    assert user.email == "hi@me.com"
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser


@pytest.mark.django_db
def test_super_user_create_with_override() -> None:
    """Test creation of regular user.

    Test to make sure we can't override staff and superuser.
    """
    with pytest.raises(ValueError):
        models.User.objects.create_superuser(
            "Jane Smith", "hi@me.com", "mypass", is_staff=False, is_superuser=True
        )

    with pytest.raises(ValueError):
        models.User.objects.create_superuser(
            "Jane Smith", "hi@me.com", "mypass", is_staff=True, is_superuser=False
        )
