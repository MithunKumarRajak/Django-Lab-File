from django.shortcuts import render, redirect
from .forms import StudentForm, CourseSelectForm
from .models import Course


def home(request):
    return render(request, "RegistrationSystem/home.html")


def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # saves student and many-to-many courses
            return redirect('rs_course_students')
    else:
        form = StudentForm()

    return render(request, "RegistrationSystem/register_student.html", {
        "form": form
    })


def course_students(request):
    students = None
    selected_course = None

    if request.method == "POST":
        form = CourseSelectForm(request.POST)
        if form.is_valid():
            selected_course = form.cleaned_data['course']
            students = selected_course.students.all()
    else:
        form = CourseSelectForm()

    context = {
        "form": form,
        "students": students,
        "selected_course": selected_course,
    }
    return render(request, "RegistrationSystem/course_students.html", context)
