from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Book
from display import models
from .forms import StudentForm, BookForm
from django.shortcuts import render, redirect
from .models import Student
from django.db.models import Q


def home(request):
    return render(request, "library/home.html")


def about(request):
    return render(request, "library/about.html")


def contact(request):
    return render(request, "library/contact.html")


def student_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        students = Student.objects.filter(
            Q(name__icontains=search_query) |
            Q(course__icontains=search_query) |
            Q(email__icontains=search_query)
        )

    else:
        students = Student.objects.all()

    return render(request, "library/student_list.html", {
        "students": students,
        "search_query": search_query
    })


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save student record
            return redirect("student_list")
    else:
        form = StudentForm()

    return render(request, "library/add_student.html", {"form": form})


def students_with_books(request):
    students = Student.objects.prefetch_related('books')
    return render(request, "library/student_books.html", {"students": students})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students_books")  # After add book
    else:
        form = BookForm()

    return render(request, "library/add_book.html", {"form": form})


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)

    return render(request, "library/edit_student.html", {"form": form})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("students_books")
    else:
        form = BookForm(instance=book)

    return render(request, "library/edit_book.html", {"form": form})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "library/confirm_delete_student.html", {"student": student})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("students_books")

    return render(request, "library/confirm_delete_book.html", {"book": book})
