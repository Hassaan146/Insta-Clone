from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class CommentSerializer(ModelSerializer):
    liked_by = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )
    class Meta:
        model = Comments
        fields = '__all__'


class PostSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    user = serializers.CharField(source='user.username', read_only=True)
    liked_by = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )
    class Meta:
        model = Post
        fields = '__all__'

class FeedSerializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'