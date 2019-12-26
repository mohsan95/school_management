from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('students', views.StudentView)
router.register('sections', views.SectionView)
router.register('courses', views.CourseView)

urlpatterns = [
    path('', include(router.urls)),
]
