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
