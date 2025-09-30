
from django.contrib import admin
from django.urls import path, include
from about.views import about, home 
# Django app folder names are case-sensitive
from display_time.views import display_time, twentyfour
from display.views import fruit_student, fruit_student_api, fruit_student_page, article_student
# from display.views import fruit_student_api # above mention
from registration.views import student_register , registration 
from vegetable.views import vegetable




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # render karke banaya hai and In this project, this is home page as default page
    path('about/', about, name='about'),  # httpResponse
    path('display_time/', display_time, name='display_time'),
    path('twentyfour/', twentyfour, name='twentyfour'),
    path('fruit_student/', fruit_student, name='fruit_student'),
    path('fruit_student/api/', fruit_student_api, name='fruit_student_api'),
    path('fruit_student_page/', fruit_student_page, name='fruit_student_page'),
    path('article_student/', article_student, name='article_student'),
    path('registration/', registration, name='registration'),
    path('student_register/', student_register, name='student_register'),
    path('vegetable/', vegetable, name='vegetable'),



]
