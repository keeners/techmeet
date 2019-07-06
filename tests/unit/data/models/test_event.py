"""Test Event model."""

from tests import factories


def test_str(event_factory: factories.EventFactory) -> None:
    """Test that the string representation returns a valid str."""
    event = event_factory.build(name="Some event")
    assert str(event) == "Some event"
