from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return HttpResponse("""<p>My Nmae is Mithun Kumar Rajak</p>
                        <h1>Welcome to the JLU!</h1>
                        """)


def home_page(request):
    return render(request, "index.html")
