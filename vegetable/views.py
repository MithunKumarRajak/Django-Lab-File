from django.shortcuts import render

# Create your views here.


def vegetable(request):
    vegetables = ["Aalu", "Aalu", "Aalu", "Aalu", "Aalu"]
    students = ["Mithun", "Kumar", "Rajak", "JLU", "Bhopal"]

    data = {
        "vegetables": vegetables,
        "students": students
    }

    return render(request, 'vegetable/vegetable.html', data)
