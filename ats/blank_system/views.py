from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.template import RequestContext
import ats.urls
from blank_system.forms import blank_form
from blank_system.models import blank
# Create your views here.



def create_blanks(request):
    if request.method == 'POST':
        #initializes the data from the form to the value form
        form = blank_form(data=request.POST)
        batch = request.POST.get("batch", "")
        if form.is_valid():
            for b in range(int(batch)):
                form.save()
                form.instance = None
                form = blank_form(data=request.POST)
            return render(request, "create_blanks.html")
        else:
            return render(request, "create_blanks.html")
    else:
        form = blank_form
        return render(request, "create_blanks.html", {'form':form})

def blanks(request):
    blanks = blank.objects.all()
    context = {
        'blanks': blanks,
    }
    return render(request, 'blanks.html', context)

