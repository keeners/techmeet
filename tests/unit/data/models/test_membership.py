"""Test Membership model."""

from tests import factories


def test_str(membership_factory: factories.MembershipFactory) -> None:
    """Test that the string representation returns a valid str."""
    membership = membership_factory.build(
        tech_group__name="Python", user__email="mail@example.com"
    )
    assert str(membership) == "mail@example.com is a member of Python"
