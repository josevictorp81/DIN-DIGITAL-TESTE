from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth.models import User

from .serializes import UserSerializers

class UserViewset(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
