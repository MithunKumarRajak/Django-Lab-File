from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="rs_home"),
    path("register/", views.register_student, name="rs_register_student"),
    path("course-students/", views.course_students, name="rs_course_students"),
]
