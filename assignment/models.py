from django.db import models
from django.contrib.auth import get_user_model
from course.models import Course

class Assignment(models.Model):
    
    
    title=models.CharField(max_length=50)
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    date=models.DateTimeField(auto_now=False)
    description=models.TextField(blank=True)
    file= models.FileField(upload_to='files/', null=True,blank=True, verbose_name="")
    grade=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.title

