"""Core Views."""
from django.contrib.auth.models import Group, User

from rest_framework import viewsets

from .serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
