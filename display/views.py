from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def fruit_student(request):
    fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
    students = ["Mithun", "Kumar", "Rajak", "JLU", "Bhopal"]

    context = {
        "fruits": fruits,
        "students": students
    }

    # agar templates ke andar custme name rakhna hai toh settiing.py mai ye add kare eg.- 'DIRS': [BASE_DIR / 'templates'], or 'DIRS': [BASE_DIR / 'display' / 'templates']
    return render(request, "display/index.html", context)


'''
# Above question ko slove karne ke liye 4 method
1.direct httpRespone mai html return kar do 
2.template ke through render kar do 
3.database mai store kar ke backend se frontend mai bhej do 
4. httpRespone ki tarah jsonResponse reture kar do

'''

# 4 Method
# must import jsonResponse


def fruit_student_api(request):
    fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
    students = ["Mithun", "Kumar", "Rajak", "JLU", "Bhopal"]

    data = {
        "fruits": fruits,
        "students": students
    }
    return JsonResponse(data)


# Above method ke shorter way

def article_student(request):
    data = {
        "articles": ["Django Basics", "Python OOP", "Web Development", "AI Basics", "Cybersecurity"],
        "students": ["Mithun", "Kumar", "Rajak", "JLU", "Bhopal"]

    }

    return render(request, "display/article_student.html", data)


# other things

def fruit_student_page(request):
    return render(request, "display/fruit_api.html")
