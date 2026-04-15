from django.contrib import admin
from .models import Receipe, Department, StudentID, Student

# Register your models here.

admin.site.register(Receipe)

admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)