from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth.models import User

from .serializes import UserSerializer

class UserViewset(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
