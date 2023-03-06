from rest_framework import serializers
from .models import Note, Course


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ('created_at',)


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('created_at',)
