from django.db import models

from django.contrib.auth import get_user_model

class Course(models.Model):
    name=models.CharField(max_length=50)
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    sum_assignments= models.IntegerField(null=True)
    time=models.TimeField(auto_now=False)
    classes=models.IntegerField(default=0)

    def __str__(self):
        return self.name