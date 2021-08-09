from django.db import models
from django.utils.timezone import now

# Create your models here.

# Databse Model for Contact form
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=12)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Message from  ' + self.name + " - " + self.email

# Database Model for MOM page
class MOM(models.Model):
    sno = models.AutoField(primary_key=True)
    task = models.TextField()
    date = models.DateField(default=now)
    
    def __str__(self):
        return 'Meeting ' + str(self.sno) + ' on ' + str(self.date)
    