from django.urls import path
from . import views

urlpatterns = [
    path('', views.course, name='course'),
    path('', views.feedback, name='feedback'),
]
