"""Group model."""

from typing import Any

from django.db import models
from django.utils.translation import gettext_lazy as _

from domain import utils


def tech_group_folder(instance: "TechGroup", filename: str) -> str:
    """File path for group files."""
    name = "".join(x for x in instance.name if x.isalnum())
    return f"{name}/{filename}"


class TechGroup(models.Model):
    """A group that has events."""

    name = models.CharField(_("name"), max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    logo = models.FileField(_("logo"), upload_to=tech_group_folder, blank=True)

    def __str__(self) -> str:
        """Return name as a string."""
        return self.name

    def save(self, *args: Any, **kwargs: Any) -> None:
        """Save a slug on save."""
        if not self.slug:
            self.slug = utils.generate_unique_slug(TechGroup, self.name)
        super().save(*args, **kwargs)

    class Meta:  # noqa D201
        verbose_name = "group"
