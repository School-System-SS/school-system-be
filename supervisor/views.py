from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SupervisorSerializer
from .models import Supervisor
from rest_framework.parsers import JSONParser 


class getAll(APIView):
    def get(self, request):
        data = Supervisor.objects.all()
        serializer = SupervisorSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

class getOne(APIView):
    def get(self, request, pk):
        data = Supervisor.objects.get(pk=pk)
        serializer = SupervisorSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)

class createSupervisor(APIView): 
    def post(self, request):
        user = request.user.pk 
        data = request.data
        data["user"] = user 
        serializer = SupervisorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateSupervisor(APIView):
    def put(self, request, pk):
        try:
            user = Supervisor.objects.get(pk=pk)
            owner = request.user.id
            updated = JSONParser().parse(request) 
            print(updated)
            updated["owner"] = owner
            serializer = SupervisorSerializer(user, data=updated)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        except Supervisor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteSupervisor(APIView):
    def delete(self, request, pk):
        try:
            data = Supervisor.objects.get(pk=pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Supervisor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)