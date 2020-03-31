import os
from datetime import date, timedelta
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group
from django.core.management import call_command
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from ats.forms import register_form
from django.contrib.auth import logout
from blank_system.models import blank
from io import StringIO
from django.core import management
from django.template import RequestContext
from django.utils.encoding import smart_str


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


def homepage(request):
    blanks = blank.objects.filter(payment_due__range=[date.today() - timedelta(days=30), date.today()], is_sold=True, is_paid=False)
    return render(request, "homepage.html", {'blanks': blanks})


@user_passes_test(lambda u: u.groups.filter(name='system_administrator').exists())
def register_user(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            user = form.save()
            my_group = form.data['group']
            print(my_group)
            user.groups.add(my_group)
            return redirect('/')
    else:
        form = register_form
    return render(request, 'register_user.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


@user_passes_test(lambda u: u.groups.filter(name='system_administrator').exists())
def backup_database(request):
    output = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static/database.json'), 'w')
    call_command('dumpdata', format='json', indent=3, stdout=output)
    output.close()
    return render(request, "backup_database.html")



@user_passes_test(lambda u: u.groups.filter(name='system_administrator').exists())
def restore_database(request):
    if request.method == 'POST':
        file = request.FILES['file']
        with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static/input_database.json'),'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        call_command('loaddata', 'static/input_database.json')
        return render(request,  'success.html')
    else:
        return render(request, "restore_database.html")

