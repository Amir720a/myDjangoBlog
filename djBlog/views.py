from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(requst):
    return render(requst , "Home.html")

def about(requst):
    return render(requst , "About.html")