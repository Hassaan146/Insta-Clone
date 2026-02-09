from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class PostAPI(APIView):
    def post(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'msg' : serializer.data})
        return Response({'msg' : serializer.errors})
    def get(self,request,id):
        if id:
            posts = Post.objects.filter(id=id)
            serializer = PostSerializer(posts)
            return Response({'posts' : serializer.data})
        else:
            posts = Post.objects.filter(user=request.user).order_by('-created_at')
            serializer = PostSerializer(posts,many=True)
            return Response({'posts' : serializer.data})
    def delete(self,request,id):
        posts = Post.objects.filter(id=id)
        if posts.exists():
                posts.delete()
                return Response({'msg' : 'Post deleted successfully'})
        return Response({'msg' : "Invalid Id"})

class CommentAPI(APIView):
    def post(self,request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'msg' : serializer.data})
        return Response({'msg' : serializer.errors})
    def get(self,request,post_id):
            comments = Comments.objects.filter(post_id=post_id).order_by('created_at')
            serializer = CommentSerializer(data=comments)
            return Response({'comments' : serializer.data})
    def delete(self,request,id):
        if id:
            comments = Comments.objects.filter(id=id)
            if comments.exists():
                comments.delete()
                return Response({'msg' : "Comment deleted "})
            return Response({'msg' : "Invalid Id"})
class FeedAPI(APIView):
     def get(self,request,id):
        feeds = Feed.objects.filter(user=request.user).order_by('-id')
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)