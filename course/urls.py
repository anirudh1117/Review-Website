from django.urls import path
from course.views import allcourse

urlpatterns = [
    path('', allcourse, name='courseindex'),
]