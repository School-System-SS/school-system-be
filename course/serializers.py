from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Student, Teacher, CourseModel, Assignment, StudentAssignment


class StudentSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=Student.objects.all())]
            )
    class Meta:
        model = Student
        fields = ('pk', 'first_name', 'last_name', 'email', 'birthday', 'type')

class TeacherSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=Teacher.objects.all())]
            )
    class Meta:
        model = Teacher
        fields = ('pk', 'first_name', 'last_name', 'birthday', 'email', 'type')

class CourseSerializer(serializers.ModelSerializer):
    # student = StudentSerializer(many=True)
    class Meta:
        model = CourseModel
        fields = ('pk','name', 'time', 'grade_level', 'teacher', 'student')

class AssignmentSerializer(serializers.ModelSerializer):
    # students = StudentSerializer()
    class Meta:
        model = Assignment
        fields = ('pk','title', 'due_date', 'points', 'course', 'teacher')

class StudentAssignmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentAssignment
#         fields = ('attachment', 'grade', 'is_submitted', 'submitted_date', 'course', 'assignment', 'student')

    # student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())

    class Meta:
        model = StudentAssignment
        fields = ('pk', 'attachment', 'grade', 'is_submitted', 'submitted_date', 'course', 'assignment', 'student')

    