from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Supervisor

class SupervisorSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=Supervisor.objects.all())]
            )
    class Meta:
        model= Supervisor
        fields=('pk', 'type', 'first_name', 'last_name', 'email', 'birthday')
    
    # def create(self, validated_data):
    #     user = Supervisor.objects.create(
    #         first_name=validated_data['firs_tname'],
    #         last_name=validated_data['last_name'],
    #         email=validated_data['email'],
    #         birthday=validated_data['birthday'],
    #     )
    #     user.save()
    #     return user

