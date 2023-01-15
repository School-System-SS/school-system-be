from rest_framework import serializers
from .models import Assignment

class Assignmentserializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = ('pk','title', 'user', 'date', 'file','course','description','grade')
