from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')


def about(request):
    return render(request, 'myapp/about.html')


def menu(request):
    return render(request, 'myapp/menu.html')


def booking(request):
    return render(request, 'myapp/booking.html')


def contact(request):
    return render(request, 'myapp/contact.html')
