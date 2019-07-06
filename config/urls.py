"""Main url routing."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import routers

from interface.api import views
from interface.app.views import index

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"techgroups", views.TechGroupViewSet)
router.register(r"memberships", views.MembershipViewSet)
router.register(r"events", views.EventViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", index, name="app"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# catch all for React router
urlpatterns += [re_path(r"^(?:.*)/?$", index)]
