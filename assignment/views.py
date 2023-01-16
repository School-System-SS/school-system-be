from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers  import Assignmentserializer
from .models import Assignment
from rest_framework.parsers import JSONParser 


class AssignmentDataView(APIView):
    def get(self, request):
        data = Assignment.objects.all()
        cleaned_data = [i for i in data if request.user.pk == i.user.pk ]
       

        serializer = Assignmentserializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

class AssignmentCertainDataView(APIView):
    def get(self, request, pk):
        data = Assignment.objects.get(pk=pk)
        serializer = Assignmentserializer(data, context={'request': request}, many=False)
        if request.user.pk == data.user.pk:
            return Response(serializer.data)
        else: return Response(status=status.HTTP_400_BAD_REQUEST)

class AssignmentCreateView(APIView): 
    def post(self, request):
        user = request.user.pk 
        data = request.data
        data["user"] = user 
        serializer = Assignmentserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignmentUpdateView(APIView):
    def put(self, request, pk):
        try:
            owner = request.user.id
            user = Assignment.objects.get(pk=pk)
            updated = JSONParser().parse(request) 
            updated["owner"] = owner
            if request.user.pk == user.user.id: 
                serializer = Assignmentserializer(user, data=updated)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
            else:
                raise Assignment.DoesNotExist
        except Assignment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class AssignmentDeleteView(APIView):
    def delete(self, request, pk):
        try:
            data = Assignment.objects.get(pk=pk)
            if request.user.pk == data.user.pk:
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                raise Assignment.DoesNotExist
        except Assignment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)