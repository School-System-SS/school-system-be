from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Student, Teacher, CourseModel, Assignment


class StudentSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=Student.objects.all())]
            )
    class Meta:
        model = Student
        fields = ('pk', 'first_name', 'last_name', 'email', 'birthday', 'student')

class TeacherSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=Teacher.objects.all())]
            )
    class Meta:
        model = Teacher
        fields = ('pk', 'first_name', 'last_name', 'birthday', 'email', 'teacher')

class CourseSerializer(serializers.ModelSerializer):
    # student = StudentSerializer(many=True)
    class Meta:
        model = CourseModel
        fields = ('pk','name', 'time', 'grade_level', 'teacher', 'student')

class AssignmentSerializer(serializers.ModelSerializer):
    # students = StudentSerializer()
    class Meta:
        model = Assignment
        fields = ('pk','title','attachment', 'due_date', 'points', 'is_submitted', 'course', 'teacher', 'students')