from django.db import models

class Teacher(models.Model):
    t_name = models.CharField(max_length=100)
    t_age = models.IntegerField()
    t_gender = models.CharField(max_length=10)

    def __str__(self):
        return self.t_name

class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='courses'
    )

    def __str__(self):
        return f"{self.name} ({self.teacher.t_name})"

class Student(models.Model):
    s_name = models.CharField(max_length=100)
    s_class = models.CharField(max_length=50)
    s_depart = models.CharField(max_length=100)
    s_grade = models.IntegerField()
    courses = models.ManyToManyField(
        Course,
        related_name='students'
    )

    def __str__(self):
        return self.s_name
