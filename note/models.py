from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TECHNOLOGY = [
    ('REACT', 'React'),
    ('JS', 'JavaScript'),
    ('DJANGO', 'Django'),
    ('Python', 'Python')
]


class Course(models.Model):
    title = models.CharField(max_length=100, null=False)
    technology = models.CharField(max_length=50, choices=TECHNOLOGY)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Note(models.Model):
    theme = models.CharField(max_length=100, null=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='course')
    notes_class = models.TextField(null=False)
    questions_of_ideas = models.TextField(null=False)
    summary = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
