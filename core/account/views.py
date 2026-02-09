from django.shortcuts import render
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile
class RegisterAPI(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            Profile.objects.create(user=user)
            return Response({'message' : serializer.data, 'access_token' : str(refresh.access_token) , 'refresh' : str(refresh)})
        return Response({'message' :serializer.errors})
    


class LoginAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                return Response({'message': 'Invalid username or password'})
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful',
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            })
        return Response({'message': serializer.errors})
class LogoutAPI(APIView):
    def post(self,request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message' : "User logged out"})
        except Exception as e:
            return Response({'msg' : str(e)})

class ProfileAPI(APIView):
    def post(self,request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message' : serializer.data})
        return Response({'msg' : serializer.errors})
    def get(self,request,id):
        profile = Profile.objects.get(id=id)
        if profile:
            serializer = ProfileSerializer(profile)
            return Response({'msg':serializer.data})
        return Response({'message' : "Profile not found"})
    