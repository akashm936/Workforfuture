from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def empreg(request):
    return render(request,"emplyee-reg.html") 

def bussinessreg(request):
    return render(request,"buss-reg.html") 