from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Story
from .serializers import StorySerializer

# Create your views here.


class StoryAPI(APIView):
    def post(self,request):
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'msg' :serializer.data})
        return Response({'msg' : serializer.errors})
    def get(self,request,id=None):
        if id:
            try:
                story = Story.objects.get(id=id)
                serializer = StorySerializer(story,context={'request': request})
                return Response(serializer.data)
            except Story.DoesNotExist:
                return Response({'msg' : 'Story not found'})
        else:
            stories = Story.objects.filter(user=request.user).order_by('-id')
            serializer = StorySerializer(stories, many=True, context={'request': request})
            return Response(serializer.data)
    def delete(self,request,id):
        try:
            story = Story.objects.get(id=id,user=request.user)
            story.delete()
            return Response({'msg' :"Story deleted Successfully"})
        except Story.DoesNotExist:
            return Response({'msg' : "Story not found"})
        