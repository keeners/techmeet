"""Shared utilities."""

from django.utils.text import slugify
from typing import Type


def generate_unique_slug(klass: Type, field: str) -> str:
    """Return a unique slug.

    return unique slug if origin slug is exist.
    eg: `foo-bar` => `foo-bar-1`
    """
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = '%s-%d' % (origin_slug, numb)
        numb += 1
    return unique_slug
