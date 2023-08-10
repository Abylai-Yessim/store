from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

menu = [
    {'title': 'Home', 'url': 'home'},
    {'title': 'About us', 'url': 'about'},
    {'title': 'Contacts', 'url': 'contact'},

]

def index(request):

    data = {
        'title': 'Главная', 
        'menu': menu, 
        'people': Product.objects.all()

    }
    return render(request, 'market/index.html', data) 

def about(request):
    data={
        'menu': menu
    }
    return render(request, 'market/about.html', data)


def contact(request):
     data={
        'menu': menu
    }
     return render(request, 'market/contact.html', data)
