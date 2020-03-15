from datetime import date

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.template import RequestContext
import ats.urls
from blank_system.forms import blank_form, assign_blank_form, register_customer_form, register_card_form, sell_form, \
    add_currency_form, stock_turnover_form
from blank_system.models import blank, customer, card, currency, assigned_range, stock_turnover_report, created_range


@user_passes_test(lambda u: u.groups.filter(name='system_administrator').exists())
def create_blanks(request):
    if request.method == 'POST':
        # initializes the data from the form to the value form
        form = blank_form(data=request.POST)
        crtd_range = created_range()
        batch = request.POST.get("batch", "")
        if form.is_valid():
            blankie = blank.objects.last()
            crtd_range.range_from = blankie.number + 1
            crtd_range.range_to = blankie.number + int(batch)
            crtd_range.save()
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
            assigned_r = assigned_range()
            assigned_r.range_from = int(from_value)
            assigned_r.range_to = int(to_value)
            assigned_r.agent = form.instance.advisor
            for b in blanks:
                assigned_r.date = b.date
                break
            assigned_r.save()
            for b in blanks:
                if b.number >= int(from_value) and b.number <= int(to_value):
                    print(form.instance.advisor)
                    b.advisor = form.instance.advisor
                    b.commission_rate = form.instance.commission_rate
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
    if request.method == 'POST':
        _sell_form = sell_form(data=request.POST, instance=blanket)
        _create_card_form = register_card_form(data=request.POST)
        if _sell_form.is_valid() and _create_card_form.is_valid():
            _sell_form.save()
            # returns the current customer in the form
            current_customer = customer.objects.get(pk=_sell_form.instance.blank_customer.name)
            _create_card_form.save()
            # sets the card for the customer to the card from the form
            card_customer = card.objects.get(pk=_create_card_form.instance.number)
            current_customer.card_info.add(card_customer)
            return render(request, 'blanku_by_card.html',
                          {'sell_form': _sell_form, 'blank': blanket, 'card_form': _create_card_form})
        else:
            print('error')
            return render(request, 'homepage.html')
    else:
        print('send')
        _sell_form = sell_form(data=request.POST, instance=blanket)
        _create_card_form = register_card_form(data=request.POST)
        return render(request, 'blanku_by_card.html',
                      {'sell_form': _sell_form, 'blank': blanket, 'card_form': _create_card_form})


def blanku_by_cash(request, number):
    blanket = blank.objects.get(pk=number)
    if request.method == 'POST':
        form = sell_form(data=request.POST, instance=blanket)
        if form.is_valid():
            form.save()
            return render(request, 'blanku_by_cash.html', {'form': form, 'blank': blanket})
        else:
            print('error')
            return render(request, 'homepage.html')
    else:
        print('send')
        form = sell_form(data=request.POST, instance=blanket)
        return render(request, 'blanku_by_cash.html', {'form': form, 'blank': blanket})


def add_currency(request):
    if request.method == 'POST':
        form = add_currency_form(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "add_currency.html")
        else:
            return render(request, "add_currency.html")
    else:
        form = add_currency_form
        return render(request, "add_currency.html", {'form': form})


def create_stock_turnover_report(request):
    if request.method == 'POST':
        form = stock_turnover_form(data=request.POST)
        report = stock_turnover_report()
        ranges = assigned_range.objects.filter(date__range=[form['date_from'].value(), form['date_to'].value()])
        created_ranges = created_range.objects.filter(date__range=[form['date_from'].value(), form['date_to'].value()])
        if form.is_valid():
            report.date_from = form.instance.date_from
            report.date_to = form.instance.date_to
            report.save()
            all_blanks = blank.objects.filter(date__range=[form['date_from'].value(), form['date_to'].value()])
            all_blanks = list(all_blanks)
            report.blanks.add(*all_blanks)
            for r in ranges:
                blankets = blank.objects.filter(number__range=[r.range_from, r.range_to])
                i = 0
                for b in blankets:
                    if (b.is_sold):
                        i = i + 1
                r.sold_blank_count = i
                r.save()
            ranges = list(ranges)
            created_ranges = list(created_ranges)
            report.assigned_range.add(*ranges)
            report.created_range.add(*created_ranges)
            report.save()
            return render(request, "create_stock_turnover_report.html")
        else:
            return render(request, "create_stock_turnover_report.html")
    else:
        form = stock_turnover_form
        return render(request, "create_stock_turnover_report.html", {'form': form})


def view_stock_turnover_report(request, number):
    report = stock_turnover_report.objects.get(pk=number)
    assigned_ranges = report.assigned_range.all()
    for r in assigned_ranges:
        blankets = blank.objects.filter(number__range=[r.range_from, r.range_to])
        i = 0
        for b in blankets:
            if (b.is_sold):
                i = i + 1
        r.sold_blank_count = i
        r.save()
    created_ranges = report.created_range.all()

    number = 0
    print(assigned_ranges)

    return render(request, "view_stock_turnover_report.html",
                  {'assigned_ranges': assigned_ranges, 'created_ranges': created_ranges})


def reports(request):
    stock_turnover_reports = stock_turnover_report.objects.all()
    return render(request, "reports.html", {'stock_turnover_reports': stock_turnover_reports})
