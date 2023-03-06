from rest_framework import routers
from .api import NoteViewSet, CourseViewSet

router = routers.DefaultRouter()

router.register('api/notes', NoteViewSet, 'notes')
router.register('api/courses', CourseViewSet, 'courses')

urlpatterns = router.urls
