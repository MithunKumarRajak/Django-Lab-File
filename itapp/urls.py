from django.urls import path
from itapp.views import event_page
urlpatterns = [
    path('', event_page, name='event_page'),
]
