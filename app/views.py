from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')

def hometest(request):
    return render(request, 'hometest.html')

def post(request):
    return render(request, 'post.html')