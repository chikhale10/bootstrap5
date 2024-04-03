from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def login(request):
    return render(request,"login.html")

def Registration(request):
    return render(request,"Registration.html")

def ContactUs(request):
    return render(request,"ContactUs.html")

def AboutUs(request):
    return render(request,"AboutUs.html")
