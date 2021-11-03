"""A meetup, an event, a social."""

from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    """A basic event model.

    We'll start with some basics for start and end dates and some markdown text.
    """

    name = models.CharField(_("name"), max_length=255)
    tech_group = models.ForeignKey(
        "data.TechGroup", on_delete=models.CASCADE, related_name=_("events")
    )
    start = models.DateTimeField(_("start"), null=True, blank=True)
    end = models.DateTimeField(_("end"), null=True, blank=True)
    description = models.TextField(_("description"), blank=True)

    def __str__(self) -> str:
        """Return string representation."""
        return self.name
