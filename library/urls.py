from .views import add_student, add_book, students_with_books, edit_student, edit_book
from django.urls import path
from .views import add_book, student_list
from .views import students_with_books, delete_student, delete_book
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("students-books/", students_with_books, name="students_books"),
    path("student_list/", student_list, name="student_list"),
    path("add-student/", add_student, name="add_student"),
    path("add-book/", add_book, name="add_book"),
    path("students-books/", students_with_books, name="students_books"),
    path("add-student/", add_student, name="add_student"),
    path("edit-student/<int:pk>/", edit_student, name="edit_student"),

    path("add-book/", add_book, name="add_book"),
    path("edit-book/<int:pk>/", edit_book, name="edit_book"),

    path("students-books/", students_with_books, name="students_books"),
    path("delete-book/<int:pk>/", delete_book, name="delete_book"),

    path("delete-student/<int:pk>/", delete_student, name="delete_student"),



]
