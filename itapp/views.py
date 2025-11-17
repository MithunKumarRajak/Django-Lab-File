from django.shortcuts import render

# Create your views here.

def event_page(request):
    materials = ["Laptop", "Mouse", "Keyboard", "USB", "Charger", "Cable", "HDMI Cable",
                 "USB Cable", "Ethernet Cable", "Wifi Cable", "SD Card", "USB Drive"]
    selected_students = ["Mithun Kumar", "Kaushik Sharma",
                         "Aditya Singh", "Mohan Gupta", "Vikas Gupta"]

    context = {
        'materials': materials,
        'students': selected_students
    }
    return render(request, 'itapp/event.html', context)
