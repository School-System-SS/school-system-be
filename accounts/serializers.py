from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'is_teacher','is_student', 'is_supervisor')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        is_teacher = validated_data.get("is_teacher", False)
        is_student = validated_data.get("is_student", False)
        is_supervisor = validated_data.get("is_supervisor", False)
        if not (is_teacher or is_student or is_supervisor):
            raise serializers.ValidationError("One of is_teacher or is_student or is_supervisor should be true")
        user = CustomUser.objects.create(
            username=validated_data['username'],
            is_teacher=is_teacher,
            is_student=is_student,
            is_supervisor=is_supervisor,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields="__all__"