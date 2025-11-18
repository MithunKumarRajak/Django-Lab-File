from django.urls import path
from .views import student_list
from .views import add_student

urlpatterns = [
    path("student_list/", student_list, name="student_list"),
    path("add-student/", add_student, name="add_student"),
]
