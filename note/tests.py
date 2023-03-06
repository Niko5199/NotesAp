from django.test import TestCase
from .models import Course


class CourseTest(TestCase):
    def setUp(self):
        Course.objects.create(title='Curso Django', technology='Python')

    def test_course_find_Django(self):
        course1 = Course.objects.get(title='Curso Django')
        self.assertEqual(course1.title, 'Curso Django')
