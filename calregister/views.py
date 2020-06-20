from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'calregister/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'calregister/about.html', {'title': 'About'})

def bookAppointment(request):
    return render(request, 'calregister/book.html', {'title': 'Book Appointment'})