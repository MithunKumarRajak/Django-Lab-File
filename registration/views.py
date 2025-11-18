from django.shortcuts import render, redirect
from .forms import StudentForm, CourseSelectForm
from .models import Course


def register(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courseStudents')

    else:
        form = StudentForm()

    return render(request, "registration/register.html", {'form': form})


def courseStudents(request):
    form = CourseSelectForm(request.POST or None)
    students = None

    if request.method == "POST" and form.is_valid():
        course = form.cleaned_data['course']
        students = course.students.all()

    return render(request, "registration/course_students.html", {
        'form': form,
        'students': students,
    })
