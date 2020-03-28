from datetime import date, timedelta

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.template import RequestContext
import ats.urls
from blank_system.forms import blank_form, assign_blank_form, register_customer_form, register_card_form, sell_form, \
    add_currency_form, stock_turnover_form, individual_sales_form_manager, individual_sales_form_agent, \
    global_sales_form, gbp_report_form
from blank_system.models import blank, customer, card, currency, assigned_range, stock_turnover_report, created_range, \
    individual_sales_report, global_sales_report, gbp_report


@user_passes_test(lambda u: u.groups.filter(name='system_administrator').exists())
def create_blanks(request):
    if request.method == 'POST':
        # initializes the data from the form to the value form
        form = blank_form(data=request.POST)
        crtd_range = created_range()
        batch = request.POST.get("batch", "")
        if form.is_valid():
            if blank.objects.last() != None:
                blankie = blank.objects.last()
                number = blankie.number + 1
            else:
                number = 1
            crtd_range.range_from = number
            crtd_range.range_to = number + int(batch)
            crtd_range.type = form.instance.type
            for b in range(int(batch)):
                m = form.save()
                form.instance = None
                form = blank_form(data=request.POST)
                blankie = m
                number = blankie.number + 1
                crtd_range.range_from = number - 1
                crtd_range.range_to = number + int(batch) - 2
                break
            for b in range(int(batch) - 1):
                form.save()
                form.instance = None
                form = blank_form(data=request.POST)
            crtd_range.save()
            return render(request, "success.html")
        else:
            return render(request, "error.html")
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
        blanks = blank.objects.filter(number__range=[int(from_value), int(to_value)])
        if form.is_valid():
            assigned_r = assigned_range()
            assigned_r.range_from = int(from_value)
            assigned_r.range_to = int(to_value)
            assigned_r.agent = form.instance.advisor
            for b in blanks:
                assigned_r.date = b.date
                assigned_r.type = b.type
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
        return render(request, 'success.html')
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
            return render(request, "success.html")
        else:
            return render(request, "error.html")
    else:
        form = register_customer_form
        return render(request, "register_customer.html", {'form': form})


@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(
    name='travel_advisor').exists())
def my_blanks(request):
    current_user = request.user
    blanks = blank.objects.filter(advisor=current_user)
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
            return render(request, "success.html")
        else:
            return render(request, "error.html")
    else:
        form = register_card_form
        return render(request, "register_card.html", {'form': form})


@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(
    name='travel_advisor').exists())
def blanku_by_card(request, number):
    blanket = blank.objects.get(pk=number)
    if request.method == 'POST':
        _sell_form = sell_form(data=request.POST, instance=blanket)
        _create_card_form = register_card_form(data=request.POST)
        if _sell_form.is_valid() and _create_card_form.is_valid():
            if _sell_form.instance.discount is not None:
                blanket.price = blanket.price - _sell_form.instance.discount
            blanket.is_sold = True
            if _sell_form.instance.payment_due is None:
                blanket.payment_due = date.today() + timedelta(days=30)
            _sell_form.save()
            # returns the current customer in the form
            current_customer = customer.objects.get(pk=_sell_form.instance.blank_customer.name)
            _create_card_form.save()
            # sets the card for the customer to the card from the form
            card_customer = card.objects.get(pk=_create_card_form.instance.number)
            current_customer.card_info.add(card_customer)
            blanket.blank_card = card_customer
            blanket.paid_by_card = True
            blanket.save()
            return render(request, 'success.html',
                          {'sell_form': _sell_form, 'blank': blanket, 'card_form': _create_card_form})
        else:
            print('error')
            return render(request, 'error.html')
    else:
        print('send')
        _sell_form = sell_form(data=request.POST, instance=blanket)
        _create_card_form = register_card_form(data=request.POST)
        return render(request, 'blanku_by_card.html',
                      {'sell_form': _sell_form, 'blank': blanket, 'card_form': _create_card_form})


@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(
    name='travel_advisor').exists())
def blanku_by_cash(request, number):
    blanket = blank.objects.get(pk=number)
    if request.method == 'POST':
        form = sell_form(data=request.POST, instance=blanket)
        if form.is_valid():
            if form.instance.discount is not None:
                blanket.price = blanket.price - form.instance.discount
            blanket.is_sold = True
            if form.instance.payment_due is None:
                blanket.payment_due = date.today() + timedelta(days=30)
            blanket.save()
            form.save()
            return render(request, 'success.html', {'form': form, 'blank': blanket})
        else:
            print('error')
            return render(request, 'error.html')
    else:
        print('send')
        form = sell_form(data=request.POST, instance=blanket)
        return render(request, 'blanku_by_cash.html', {'form': form, 'blank': blanket})


@user_passes_test(lambda u: u.groups.filter(name='system_administrator').exists())
def add_currency(request):
    if request.method == 'POST':
        form = add_currency_form(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
        else:
            return render(request, "error.html")
    else:
        form = add_currency_form
        return render(request, "add_currency.html", {'form': form})


@user_passes_test(
    lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(name='system_administrator').exists())
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
            return render(request, "success.html")
        else:
            return render(request, "error.html")
    else:
        form = stock_turnover_form
        return render(request, "create_stock_turnover_report.html", {'form': form})


@user_passes_test(
    lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(name='system_administrator').exists())
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


@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(
    name='travel_advisor').exists() or u.groups.filter(name='system_administrator').exists())
def reports(request):
    stock_turnover_reports = stock_turnover_report.objects.all()
    individual_sales_reports = individual_sales_report.objects.all()
    global_sales_reports = global_sales_report.objects.all()
    return render(request, "reports.html", {'stock_turnover_reports': stock_turnover_reports,
                                            'individual_sales_reports': individual_sales_reports,
                                            'global_sales_reports': global_sales_reports})


@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(
    name='travel_advisor').exists() or u.groups.filter(name='system_administrator').exists())
def create_reports(request):
    return render(request, "create_reports.html")


@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(
    name='travel_advisor').exists())
def create_individual_sales_report(request):
    current_user = request.user
    report = individual_sales_report()
    if current_user.groups.filter(name__in=['travel_advisor']).exists():
        form = individual_sales_form_agent(data=request.POST)
    else:
        form = individual_sales_form_manager(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            report.date_from = form.instance.date_from
            report.date_to = form.instance.date_to
            report.type = form.instance.type
            if current_user.groups.filter(name__in=['travel_advisor']).exists():
                report.agent = current_user
            else:
                report.agent = form.instance.agent
            report.save()
            return render(request, "success.html", {'form': form})
        else:
            return render(request, "error.html", {'form': form})
    else:
        return render(request, "create_individual_sales_report.html", {'form': form})


@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(
    name='travel_advisor').exists())
def view_individual_sales_report(request, number):
    report = individual_sales_report.objects.get(pk=number)
    if report.type == "Interline":
        blanks_report = blank.objects.filter(date__range=[report.date_from, report.date_to], is_sold=True,
                                             type__in=["440", "444", "420"])
    if report.type == "Domestic":
        blanks_report = blank.objects.filter(date__range=[report.date_from, report.date_to], is_sold=True,
                                             type__in=["201", "101"])
    total_price = 0
    total_price_local = 0
    total_commission = 0
    total_paid = 0
    total_paid = 0
    num = 0
    for b in blanks_report:
        total_price = b.price + total_price
        if b.blank_currency is not None:
            total_price_local = (b.price * b.blank_currency.rate) + total_price_local
        num = num + 1
        if b.is_paid:
            total_commission = (b.price * b.commission_rate / 100) + total_commission
            total_paid = total_paid + b.price
    return render(request, "view_individual_sales_report.html",
                  {'blanks_report': blanks_report, 'total_price': total_price, 'num': num,
                   'total_price_local': total_price_local, 'total_commission': total_commission,
                   'total_paid': total_paid})


@user_passes_test(
    lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(name='system_administrator').exists())
def create_global_sales_report(request):
    report = global_sales_report()
    form = global_sales_form(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            report.date_from = form.instance.date_from
            report.date_to = form.instance.date_to
            report.type = form.instance.type
            report.save()
            return render(request, "success.html", {'form': form})
        else:
            return render(request, "error.html", {'form': form})
    else:
        return render(request, "create_individual_sales_report.html", {'form': form})


@user_passes_test(
    lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(name='system_administrator').exists())
def view_global_sales_report(request, number):
    report = global_sales_report.objects.get(pk=number)
    if report.type == "Interline":
        blanks_report = blank.objects.filter(date__range=[report.date_from, report.date_to], is_sold=True,
                                             type__in=["440", "444", "420"])
    if report.type == "Domestic":
        blanks_report = blank.objects.filter(date__range=[report.date_from, report.date_to], is_sold=True,
                                             type__in=["201", "101"])
    total_price = 0
    total_price_local = 0
    total_commission = 0
    total_paid = 0
    total_paid = 0
    num = 0
    for b in blanks_report:
        total_price = b.price + total_price
        if b.blank_currency is not None:
            total_price_local = (b.price * b.blank_currency.rate) + total_price_local
        num = num + 1
        if b.is_paid:
            total_commission = (b.price * b.commission_rate / 100) + total_commission
            total_paid = total_paid + b.price
    return render(request, "view_global_sales_report.html",
                  {'blanks_report': blanks_report, 'total_price': total_price, 'num': num,
                   'total_price_local': total_price_local, 'total_commission': total_commission,
                   'total_paid': total_paid})


@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(
    name='travel_advisor').exists())
def refund(request, number):
    blankie = blank.objects.get(pk=number)
    blankie.is_refunded = True
    blankie.price = 0
    blankie.save()
    return render(request, 'refund.html')


@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(
    name='travel_advisor').exists())
def set_paid(request, number):
    blankie = blank.objects.get(pk=number)
    blankie.is_paid = True
    blankie.save()
    return render(request, 'set_paid.html')


@user_passes_test(
    lambda u: u.groups.filter(name='system_administrator').exists())
def delete_blanks(request):
    if request.method == 'POST':
        from_value = request.POST.get("from_value", "")
        to_value = request.POST.get("to_value", "")
        created_rang = created_range.objects.filter(range_from__range=[int(from_value), int(to_value)], range_to__range=[int(from_value), int(to_value)])
        assigned_rang = assigned_range.objects.filter(range_from__range=[int(from_value), int(to_value)], range_to__range=[int(from_value), int(to_value)])
        created_rang.delete()
        assigned_rang.delete()
        blanket = blank.objects.filter(number__range=[int(from_value), int(to_value)])
        blanket.delete()
        return render(request, 'success.html')
    else:
        return render(request, 'delete_blanks.html')


@user_passes_test(
    lambda u: u.groups.filter(name='system_administrator').exists())
def create_blanks_with_range(request):
    crtd_range = created_range()
    form = blank_form(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            from_value = request.POST.get("from_value", "")
            to_value = request.POST.get("to_value", "")
            crtd_range.range_from = from_value
            crtd_range.range_to = to_value
            crtd_range.type = form.instance.type
            crtd_range.save()
            for i in range(int(from_value), int(to_value) + 1):
                blankie = blank()
                blankie.number = i
                blankie.price = form.instance.price
                blankie.type = form.instance.type
                blankie.save()
                print(i)
                print(blankie)
            return render(request, "success.html")
        else:
            return render(request, "error.html")
    else:
        return render(request, 'create_blanks_with_range.html', {'form': form})


@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(
    name='travel_advisor').exists())
def search_for_a_blank(request):
    if request.method == 'POST':
        from_value = request.POST.get("blank_no", "")
        return individual_blank(request, int(from_value))
    else:
        return render(request, 'search_for_a_blank.html')


@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.groups.filter(
    name='travel_advisor').exists())
def individual_blank(request, number):
    blanket = blank.objects.filter(number=number)
    if blanket is not None:
        return render(request, 'individual_blank.html', {'blanket': blanket})
    else:
        return render(request, 'error.html')


@user_passes_test(lambda u: u.groups.filter(name='manager').exists())
def create_gbp_report(request):
    form = gbp_report_form(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, "success.html")
        else:
            return render(request, "error.html")
    else:
        return render(request, "create_gbp_report.html", {'form': form})


@user_passes_test(lambda u: u.groups.filter(name='manager').exists())
def view_gbp_report(request, number):
    report = gbp_report.objects.get(pk=number)
    blanks420 = blank.objects.filter(date__range=[report.date_from, report.date_to], is_sold=True, type__in=["420"])
    blanks444 = blank.objects.filter(date__range=[report.date_from, report.date_to], is_sold=True, type__in=["444"])
    rates = currency.objects.filter(date__range=[report.date_from, report.date_to])
    for r in rates:
        count420 = 0
        count444 = 0
        total_price = 0
        for b in blanks420:
            if b.blank_currency == r:
                count420 = count420 + 1
                total_price = total_price + b.price
        for b in blanks444:
            if b.blank_currency == r:
                count444 = count444 + 1
                total_price = total_price + b.price
        r.count_420 = count420
        r.count_444 = count444
        r.total = total_price
        r.save()
    rates = currency.objects.filter(date__range=[report.date_from, report.date_to])
    return render(request, "view_gbp_report.html", {'rates': rates, 'report': report})

