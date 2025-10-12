from django.urls import path
from . import views

urlpatterns = [
    # agar yaha blank '' chhode hai to default view chalega otherwise / raha toh / bhi url mai lagana padega browser url mai
    path('', views.courseFee, name='courseFee'),
]
