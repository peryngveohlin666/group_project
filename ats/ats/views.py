from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext


def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, "homepage.html")
        else:
            return render(request, "homepage.html")
    else:
        if request.user.is_authenticated:
            return render(request, "homepage.html")
        else:
            form = AuthenticationForm()
            return render(request, "index.html", {'form': form})


# @user_passes_test(test here)
def homepage(request):
    return render(request, "homepage.html")
