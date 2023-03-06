from .models import Note, Course
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import NoteSerializer, CourseSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    permission_classes = [AllowAny]
    serializer_class = NoteSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CourseSerializer
