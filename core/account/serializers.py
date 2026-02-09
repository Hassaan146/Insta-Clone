from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)


class ProfileSerializer(ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'followers', 'following', 'dp']