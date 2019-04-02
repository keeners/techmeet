"""Test utils functions."""

import pytest
from domain.utils import generate_unique_slug

from data import models
from tests import factories


@pytest.mark.django_db
def test_first_slug() -> None:
    """Test that we get a simple slugified word."""
    slug = generate_unique_slug(models.TechGroup, "Python")
    assert slug == "python"


@pytest.mark.django_db
def test_second_slug() -> None:
    """Test that we get a simple slugified word."""
    factories.TechGroupFactory(slug="python")
    slug = generate_unique_slug(models.TechGroup, "Python")
    assert slug == "python-1"
