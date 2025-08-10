from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to My First Django App!")
def home(request):
    return HttpResponse("Hello World")
def about(request):
    return HttpResponse("This is the about page")