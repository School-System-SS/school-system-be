from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields=['pk','name', 'user','sum_assignments','time','classes']
