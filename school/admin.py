from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Teacher, Student

admin.site.register(Teacher)
admin.site.register(Student)
