from django.shortcuts import render
from .models import courses


def course(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        course = request.POST.get("course")
        start_date = request.POST.get("start_date")

        if full_name and email and phone and course and start_date:
            courses.objects.create(
                full_name=full_name,
                email=email,
                phone=phone,
                course=course,
                start_date=start_date
            )
            return render(request, "courses/success.html", {"name": full_name})
    return render(request, "courses/index.html")

