from .models import Student
from django.shortcuts import render
# Create your views here.


def registration(request):
    students = [" ", "Mithun", "Kumar", "Rajak"]
    courses = [" ", "Python Basics",
               "Cybersecurity (v12)", "Web Dev", " Django", "Java", "Js", "OS"]

    context = {
        "students": students,
        "courses": courses
    }
    return render(request, "registration/index.html", context)

# trying to add data to database

def student_register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        course = request.POST.get("course")

        # basic empty check (optional)
        if name and email and course:
            Student.objects.create(name=name, email=email, course=course)
            return render(request, "registration/student.html", {
                "success": True
            })

    return render(request, "registration/student.html")
