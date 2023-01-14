from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import CourseSerializer
from .models import Course


class CourseListView(ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class= CourseSerializer

class CourseDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class= CourseSerializer