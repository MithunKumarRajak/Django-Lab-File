from django.shortcuts import render, redirect
from .models import courses
from .forms import FeedbackForm


def course(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        course = request.POST.get("course")
        start_date = request.POST.get("start_date")
    return render(request, "courses/index.html")


def feedback(request):
    submitted = False  # Flag to show thank-you message
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to same form with query param
            return redirect('/feedback/?submitted=True')
    else:
        form = FeedbackForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'courses/feedback.html', {'form': form, 'submitted': submitted})

#


def course_list(request):
    courses = [
        "C Programming",
        "Python Programming",
        "Database Management System",
        "Web Development",
        "Data Structures",
        "Django",
        "Operations System",

    ]

    students = [
        "Mithun Kumar",
        "Kaushik Sharma",
        "Mohan Gupta",
        "Aditya Singh",
        "Dilip singh",
        "Mithun Kumar Rajak",
        "Mohit Rajak",
    ]

    context = {
        'courses': courses,
        'students': students,
    }

    return render(request, 'courses/course.html', context)
