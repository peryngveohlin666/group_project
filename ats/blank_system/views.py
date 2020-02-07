from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.template import RequestContext
import ats.urls
from blank_system.forms import blank_form

# Create your views here.
def create_blanks(request):
    if request.method == 'POST':
        #initializes the data from the form to the value form
        form = blank_form(data=request.POST)
        if form.is_valid():
            new_blank = form.save();
            return render(request, "create_blanks.html")
        else:
            return render(request, "create_blanks.html")
    else:
        form = blank_form
        return render(request, "create_blanks.html", {'form':form})

