from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')
def signup(request):
    return render(request, 'home/signup.html')
def login(request):
    return render(request, 'home/login.html')
def contact(request):
    return render(request, 'home/contact.html')
def about(request):
    return render(request, 'home/about.html')
