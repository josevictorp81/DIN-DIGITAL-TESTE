from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializes import UserSerializer, ProductSerializer
from .models import Product


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    