from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, GetUserSerializer
from rest_framework.permissions import AllowAny
from .models import CustomUser


class SignUpView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getAllUsers(APIView):
    def get(self, request):
        data = CustomUser.objects.all()
        serializer = GetUserSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)