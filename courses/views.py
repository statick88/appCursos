from rest_framework.viewsets import ModelViewSet
from .models import Course, Student
from .serializers import CourseSerializers, StudentSerializers

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

class StudentVewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
