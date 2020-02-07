from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext


def index(request):
    #checks if the user clicked the post button or just loaded the page
    if request.method == 'POST':
        #initializes the data from the form to the value form
        form = AuthenticationForm(data=request.POST)
        #checks if the form is valid and forwards you to the homepage if the form is valid
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, "homepage.html")
        #sends you to the homepage if the form is invalid but you will get an error message when you arrive there as you are not logged in
        else:
            return render(request, "homepage.html")
    else:
        #returns the home page to the user if user is authenticated already
        if request.user.is_authenticated:
            return render(request, "homepage.html")
        # returns the login page to the user if user is not authenticated
        else:
            form = AuthenticationForm()
            return render(request, "index.html", {'form': form})


# @user_passes_test(test here)
def homepage(request):
    return render(request, "homepage.html")
