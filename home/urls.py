from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('objectives/', views.objectives, name='objectives'),
    path('team/', views.team, name='team'),
    path('projects/', views.projects, name='projects'),
    path('meeting/', views.meeting, name='meeting'),
    path('gallery/', views.gallery, name='gallery'),
    path('achievements/', views.achievements, name='achievements'),
    path('contact/', views.contact, name='contact'),
]