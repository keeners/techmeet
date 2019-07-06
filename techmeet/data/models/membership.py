"""Membership model.

A user can be a member of a group.
"""
from django.conf import settings
from django.db import models


class Membership(models.Model):
    """A user is a member of a group through membership."""

    tech_group = models.ForeignKey("data.TechGroup", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return user and tech group as string."""
        return f"{self.user} is a member of {self.tech_group}"

    class Meta:  # noqa D201
        unique_together = ["tech_group", "user"]
        ordering = ["user", "date_joined"]
