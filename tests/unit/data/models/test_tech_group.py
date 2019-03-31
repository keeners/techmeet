"""Test User model."""

import pytest

from pytest_mock import MockFixture

from data import models
from tests import factories

def test_tech_group_folder_pattern() -> None:
    """Test file paths are generated correctly."""
    tech_group = models.TechGroup(name="Python &#123")
    path = models.tech_group.tech_group_folder(tech_group, "blah.tmp")
    assert path == "Python123/blah.tmp"

def test_str(tech_group_factory: factories.TechGroupFactory) -> None:
    """Test that the string representation returns the name."""
    tech_group = tech_group_factory.build(name="Python", slug="python", description="Best group ever.")
    assert str(tech_group) == "Python"

@pytest.mark.django_db
def test_slug_called(mocker: MockFixture, tech_group_factory: factories.TechGroupFactory) -> None:
    """Test slug is created if not passed."""
    mocked_slugger = mocker.patch("domain.utils.generate_unique_slug")
    mocked_slugger.return_value = "python"
    tech_group = tech_group_factory(name="Python", description="Best group ever.")
    assert mocked_slugger.called
    assert tech_group.slug == "python"
