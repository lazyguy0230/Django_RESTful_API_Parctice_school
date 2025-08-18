from rest_framework import viewsets
from .models import Teacher, Student, Course
from .serializers import TeacherSerializer, StudentSerializer, CourseSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.prefetch_related('courses__teacher')
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.select_related('teacher')
    serializer_class = CourseSerializer
