from django.urls import path
from .views import *

urlpatterns = [
    path('', course, name='course'),
    path('feedback/', feedback, name='feedback'),
    path('course_list/', course_list, name='course_list'),
]
