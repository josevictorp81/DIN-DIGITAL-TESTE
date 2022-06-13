from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'password': {'write_only': True}
        }
        model = User
        fields = ['id', 'username', 'password']
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity']
        read_only_fields = ['id']
        