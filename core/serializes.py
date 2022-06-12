from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'password': {'write_only': True}
        }
        model = User
        fields = ['id', 'username', 'password']
    
    def validate(self, attrs):
        user = User.objects.filter(username=attrs['username']).first()
        if user:
            raise serializers.ValidationError(detail='User with this username already existes!')
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user