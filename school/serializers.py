from rest_framework import serializers
from .models import Teacher, Student, Course

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        source='teacher',
        write_only=True
    )
    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher', 'teacher_id']

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    course_ids = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        many=True,
        source='courses',
        write_only=True
    )
    class Meta:
        model = Student
        fields = ["id", "s_name", "s_class", "s_depart", "s_grade", "courses", "course_ids"]
