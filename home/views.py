from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# HTML pages
def home(request):
    return render(request, 'home/home.html')