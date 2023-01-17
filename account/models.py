from django.contrib.auth.models import AbstractUser
from django.db import models
from course.models import Course
Role_Type = (
    ("Admin", "Admin"),
    ("Teacher", "Teacher"),
    ("Student", "Student"),
)
  

class CustomUser(AbstractUser):
    firstname = models.CharField(('Firt Name'), max_length=255,null=True)
    lastname = models.CharField(('Last Name'), max_length=255,null=True)
    email = models.EmailField(('Email'), max_length=255,unique=True)
    birthday=models.DateField(('Birthday'),null=True)
    role=models.CharField(
        max_length = 20,
        choices = Role_Type,
        default = 'Admin',
        null=True
        )
    courses=models.ManyToManyField(Course)
    def __str__(self):
        return self.username