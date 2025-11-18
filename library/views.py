from .forms import StudentForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Student


def student_list(request):
    students = Student.objects.all()  # Fetch all students
    return render(request, "library/student_list.html", {"students": students})


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save student record
            return redirect("student_list")
    else:
        form = StudentForm()

    return render(request, "library/add_student.html", {"form": form})
