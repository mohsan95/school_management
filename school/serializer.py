from rest_framework import serializers
from .models import Student, Section, Course


class StudentSerializer(serializers.ModelSerializer):
    section_name = serializers.CharField(source='section.name', read_only=True, required=False)

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll_no', 'contact', 'section', 'section_name', 'courses']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'code']


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'name']
