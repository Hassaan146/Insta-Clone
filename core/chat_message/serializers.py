from .models import Group,Message
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
class GroupSerializer(ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = '__all__'