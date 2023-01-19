from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Supervisor(models.Model):
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    email = models.EmailField(unique=True)
    birthday = models.DateField()
    supervisor = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.supervisor.username