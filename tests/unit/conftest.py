"""Fixtures used for user tests."""

from pytest_factoryboy import register

from tests import factories

register(factories.UserFactory)
register(factories.SuperUserFactory)
register(factories.TechGroupFactory)
register(factories.MembershipFactory)
