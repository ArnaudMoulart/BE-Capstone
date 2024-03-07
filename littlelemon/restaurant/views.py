from django.shortcuts import render
from .models import Menu

# Create your views here.

def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request, "about.html", {'content': about_content})

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, "menu.html", main_data)

def home(request):
    return render(request, 'index.html',{'current_year': 2022})

def book(request):
    return render(request, 'book.html',{'current_year': 2022})

