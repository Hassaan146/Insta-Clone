from django.shortcuts import get_object_or_404
from .models import Message, Group
from .serializers import MessageSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class MessageAPI(APIView):
# Using channels 

    # def post(self, request):
    #     serializer = MessageSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': serializer.data})
    #     return Response({'msg': serializer.errors})
    def delete(self, request, id):
        message = get_object_or_404(Message, id=id)
        message.delete()
        return Response({'msg': 'Message deleted'})
    def get(self, request, receiver=None):
        if receiver:
            messages = Message.objects.filter(receiver=receiver).order_by('-created_at')
        serializer = MessageSerializer(messages, many=True)
        return Response({'msg': serializer.data})
    def put(self, request, id):
        message = get_object_or_404(Message, id=id)
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': serializer.data})
        return Response({'msg': serializer.errors})

class GroupAPI(APIView):
    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': serializer.data})
        return Response({'msg': serializer.errors})

    def get(self, request, name=None):
        if name:
            group = get_object_or_404(Group, name=name)
            serializer = GroupSerializer(group)
        else:
            groups = Group.objects.all()
            serializer = GroupSerializer(groups, many=True)
        return Response({'msg': serializer.data})

    def put(self, request, name):
        group = get_object_or_404(Group, name=name)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': serializer.data})
        return Response({'msg': serializer.errors})
