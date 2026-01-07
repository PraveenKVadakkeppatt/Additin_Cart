from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from users.serializers import UserProfileSerializer, UserRegisterSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.



class RegisterView(APIView):
    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
    
    def patch(self,request):
        serilaizer = UserProfileSerializer(request.user, data=request.data, partial = True)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data,status=status.HTTP_200_OK)