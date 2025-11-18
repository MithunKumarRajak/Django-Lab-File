from django import forms
from .models import Student, Book


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_no', 'name', 'course', 'email']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year', 'student']
