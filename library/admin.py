from .models import Student
from django.contrib import admin
from .models import Book

admin.site.register(Book)

admin.site.register(Student)
