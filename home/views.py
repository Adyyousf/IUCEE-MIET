from IUCEEweb.settings import EMAIL_HOST_USER
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from home.models import Contact, MOM

# Create your views here.

# HTML pages

# Renders home page
def home(request):
    return render(request, 'home/home.html')

# Renders objectives page
def objectives(request):
    return render(request, 'home/objectives.html')

# Renders home page
def team(request):
    return render(request, 'home/team.html')

# Renders meet the team page
def projects(request):
    return render(request, 'home/projects.html')

# Renders gallery page
def gallery(request):
    return render(request, 'home/gallery.html')

# Renders achievements page
def achievements(request):
    return render(request, 'home/achievements.html')

# Renders contact page
def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        content = request.POST["content"]

        # conditional check form data (data Validation)
        if len(name) < 2 or len(email) < 4 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly") # alert error message
        else:
            # if the data entered is correct save it inside the contact model in database
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent") # alert success message
        
        # automated mailing system
        # sends the mail to the email id entered
        subject = 'Welcome to IUCEE MIET'
        message = f"Hi {name}, Thanks for contacting. We will contact you soon"
        email_from = settings.EMAIL_HOST_USER
        recipent_list = [email, ]
        send_mail(subject, message, email_from, recipent_list)

    return render(request, 'home/contact.html')


# Renders meeting page
def meeting(request):
    # gets the data from MOM model from the databse 
    allTasks = MOM.objects.all()
    context = {'allTasks': allTasks} # dictionary of the data queried. To be sent for rendering inside meeting.html

    return render(request, 'home/meeting.html', context)


# Renders tasks page
def tasks(request, sno):
    content = MOM.objects.filter(sno=sno) # get the object from the database where sno matches the sno returned by task
    context = {'content': content}
    return render(request, 'home/tasks.html', context)
