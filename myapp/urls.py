from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('booking/', booking, name='booking'),
    path('contact/', contact, name='contact'),
    path('grain/', grain_view, name='grain_view'),
]
