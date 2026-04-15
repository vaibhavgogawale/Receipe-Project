from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_desc = models.TextField()
    receipe_image = models.FileField(upload_to='receipe')

    def __str__(self):
        return f"Receipe Name: {self.receipe_name}"


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering = ['department']



class StudentID(models.Model):
    student_id = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.student_id



class Student(models.Model):
    department = models.ForeignKey(Department, related_name='depart', on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name='studentid', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=10)
    student_address = models.TextField(default=None)

    def __str__(self) -> str:
        return self.student_name

    class Meta:
        ordering = ['student_name']
        verbose_name = 'student'