from django.db import models
from django.contrib.auth import get_user_model

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birthday = models.DateField()
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.student.username

class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birthday = models.DateField()
    teacher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher.username

class CourseModel(models.Model):
    name = models.CharField(max_length=255)
    time = models.TimeField()
    grade_level = models.CharField(max_length=50, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
 
class Assignment(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    points = models.FloatField()
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='assignments')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='assignments')

    def __str__(self):
        return self.title

class StudentAssignment(models.Model):
    # attachment = models.FileField(upload_to='uploads/', null=True,blank=True, verbose_name="")
    attachment = models.TextField(blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)
    is_submitted = models.BooleanField(default=False, blank=True, null=True)
    submitted_date = models.DateField(blank=True, null=True,auto_now=True)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE,)

    def __str__(self):
        return self.assignment.title