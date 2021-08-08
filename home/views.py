from IUCEEweb.settings import EMAIL_HOST_USER
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from home.models import Contact

# Create your views here.

# HTML pages
def home(request):
    return render(request, 'home/home.html')

def objectives(request):
    return render(request, 'home/objectives.html')

def team(request):
    return render(request, 'home/team.html')

def projects(request):
    return render(request, 'home/projects.html')

def meeting(request):
    return render(request, 'home/meeting.html')

def gallery(request):
    return render(request, 'home/gallery.html')

def achievements(request):
    return render(request, 'home/achievements.html')

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        content = request.POST["content"]

        if len(name) < 2 or len(email) < 4 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
        
        subject = 'Welcome to IUCEE MIET'
        message = f"Hi {name}, Thanks for contacting. We will contact you soon"
        email_from = settings.EMAIL_HOST_USER
        recipent_list = [email, ]
        send_mail(subject, message, email_from, recipent_list)

    return render(request, 'home/contact.html')