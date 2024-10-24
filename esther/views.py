from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("<h1>Welcome to Esther's Django App for Git Practice</h1>")