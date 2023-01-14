from django.db import models

from django.contrib.auth import get_user_model

class Course(models.Model):
    name=models.CharField(max_length=50)
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    grade= models.IntegerField(default=0)
    time=models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.name