from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login


# don't forget to add the templates folder in setting.py
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        return render(request, "homepage.html")
    else:
        return render(request, "index.html")


# @user_passes_test(test here)
def homepage(request):
    return render(request, "homepage.html")
