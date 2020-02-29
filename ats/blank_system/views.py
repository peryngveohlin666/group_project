from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.template import RequestContext
import ats.urls
from blank_system.forms import blank_form, assign_blank_form, register_customer_form
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
        return render(request, "create_blanks.html", {'form': form})


def blanks(request):
    blanks = blank.objects.all()
    context = {
        'blanks': blanks,
    }
    return render(request, 'blanks.html', context)


def assign_blanks(request):
    if request.method == 'POST':
        form = assign_blank_form(data=request.POST)
        from_value = request.POST.get("from_value", "")
        to_value = request.POST.get("to_value", "")
        blanks = blank.objects.all()
        if form.is_valid():
            for b in blanks:
                if b.number >= int(from_value) and b.number <= int(to_value):
                    print(form.instance.advisor)
                    b.advisor = form.instance.advisor
                    b.save()
                if b.number == int(to_value):
                    break
                print(b.number)
        return render(request, 'assign_blanks.html')
    else:
        form = assign_blank_form()
        return render(request, 'assign_blanks.html', {'form':form})


def register_customer(request):
    if request.method == 'POST':
        #initializes the data from the form to the value form
        form = register_customer_form(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "register_customer.html")
        else:
            return render(request, "register_customer.html")
    else:
        form = register_customer_form
        return render(request, "register_customer.html", {'form': form})