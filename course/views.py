from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers  import CourseSerializer
from .models import Course
from rest_framework.parsers import JSONParser 
from rest_framework import status




class CourseListView(APIView):
        def get(self, request):
                    data = Course.objects.all()
                    cleaned_data = [i for i in data if request.user.pk == i.user.pk]
                    serializer = CourseSerializer(cleaned_data, context={'request': request}, many=True)
                    return Response(serializer.data)


class CertainDataView(APIView):
        def get(self, request, pk):
            data = Course.objects.get(pk=pk)
            serializer = CourseSerializer(data, context={'request': request}, many=False)
            if request.user.pk == data.user.pk:
                            return Response(serializer.data)
            else: return Response(status=status.HTTP_400_BAD_REQUEST)

class CreateView(APIView): 
        def post(self, request):
            user = request.user.pk
            data = request.data
            data["user"] = user
            serializer = CourseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UpdateView(APIView):
    def put(self, request, pk):
        try:
            owner = request.user.id
            user = Course.objects.get(pk=pk)
            updated = JSONParser().parse(request) 
            updated["user"] = owner
            if request.user.pk == user.user.id: 
                serializer = CourseSerializer(user, data=updated)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
            else:
                raise Course.DoesNotExist
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteView(APIView):
    def delete(self, request, pk):
        try:
            data = Course.objects.get(pk=pk)
            if request.user.pk == data.user.pk:
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                raise Course.DoesNotExist
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)










    

