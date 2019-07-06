"""Django admin registrations."""

from django.contrib import admin

from . import models

admin.site.register(models.Event)
admin.site.register(models.Membership)
admin.site.register(models.TechGroup)
admin.site.register(models.User)
