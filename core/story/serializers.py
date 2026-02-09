from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Story

class StorySerializer(ModelSerializer):
    likes_count = serializers.IntegerField(source = 'liked_by.count',read_only = True)
    views_count = serializers.IntegerField(source = 'viewed_by.count',read_only = True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Story
        fields = [
            'id','image','user','likes_count','views_count','created_at']
        read_only_fields = ['user', 'likes_count', 'views_count', 'created_at']

        
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)