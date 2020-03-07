from datetime import date

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.template import RequestContext
import ats.urls
from blank_system.forms import blank_form, assign_blank_form, register_customer_form, register_card_form, sell_by_cash_form
from blank_system.models import blank


@user_passes_test(lambda u: u.groups.filter(name='system_administrator').exists())
def create_blanks(request):
    if request.method == 'POST':
        # initializes the data from the form to the value form
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


@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(
    name='travel_advisor').exists() or u.groups.filter(name='system_administrator').exists())
def blanks(request):
    blanks = blank.objects.all()
    context = {
        'blanks': blanks,
    }
    return render(request, 'blanks.html', context)


@user_passes_test(
    lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(name='system_administrator').exists())
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
        return render(request, 'assign_blanks.html', {'form': form})


@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(
    name='travel_advisor').exists() or u.groups.filter(name='system_administrator').exists())
def register_customer(request):
    if request.method == 'POST':
        # initializes the data from the form to the value form
        form = register_customer_form(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "register_customer.html")
        else:
            return render(request, "register_customer.html")
    else:
        form = register_customer_form
        return render(request, "register_customer.html", {'form': form})


@user_passes_test(
    lambda u: u.groups.filter(name='travel_advisor').exists() or u.groups.filter(name='system_administrator').exists())
def my_blanks(request):
    blanks = blank.objects.all()
    current_user = request.user
    context = {
        'blanks': blanks,
        'current_user': current_user
    }
    return render(request, 'my_blanks.html', context)


@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(
    name='travel_advisor').exists() or u.groups.filter(name='system_administrator').exists())
def register_card(request):
    if request.method == 'POST':
        form = register_card_form(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "register_card.html")
        else:
            return render(request, "register_customer.html")
    else:
        form = register_card_form
        return render(request, "register_card.html", {'form': form})


def blanku_by_card(request, number):
    blanket = blank.objects.get(pk=number)
    context = {
        'blank': blanket,
    }
    return render(request, 'blanku_by_card.html', context)


def blanku_by_cash(request, number):
    blanket = blank.objects.get(pk=number)
    if request.method == 'POST':
        form = sell_by_cash_form(data=request.POST, instance=blanket)
        if form.is_valid():
            form.save()
            blanket.is_sold = True
            blanket.date_sold = date.today()
            return render(request, 'blanku_by_cash.html', {'form': form, 'blank': blanket})
        else:
            print('error')
            return render(request, 'homepage.html')
    else:
        print('send')
        form = sell_by_cash_form(data=request.POST, instance=blanket)
        return render(request, 'blanku_by_cash.html', {'form': form, 'blank': blanket})
