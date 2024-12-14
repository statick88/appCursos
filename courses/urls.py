from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, StudentVewSet

router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('students', StudentVewSet)

urlpatterns = router.urls