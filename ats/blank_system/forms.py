from django.forms import ModelForm
from django import forms
from blank_system.models import blank, customer, card, currency, assigned_range, stock_turnover_report, individual_sales_report, global_sales_report


# a form object for blanks
class blank_form(ModelForm):
    class Meta:
        #the model the form references to
        model = blank
        #the fields to fill in the form for that model
        fields = ['type', 'price']

#a form to support assigning blanks
class assign_blank_form(ModelForm):
    class Meta:
        # the model the form references to
        model = blank
        # the fields to fill in the form for that model
        fields = ['advisor', 'commission_rate']


class register_customer_form(ModelForm):
    class Meta:
        # the model the form references to
        model = customer
        # the fields to fill in the form for that model
        fields = ['is_regular', 'is_valued', 'name', 'address']


class register_card_form(ModelForm):
    class Meta:
        model = card
        fields = ['number', 'name', 'surname', 'address']


class sell_form(ModelForm):
    class Meta:
        model = blank
        fields = ['blank_customer', 'is_paid', 'payment_due', 'blank_currency', 'discount']


class add_currency_form(ModelForm):
    class Meta:
        model = currency
        fields = ['type', 'rate']


class stock_turnover_form(ModelForm):
    class Meta:
        model = stock_turnover_report
        fields = ['date_to', 'date_from']


class individual_sales_form_manager(ModelForm):
    class Meta:
        model = individual_sales_report
        fields = ['date_to', 'date_from', 'agent']


class individual_sales_form_agent(ModelForm):
    class Meta:
        model = individual_sales_report
        fields = ['date_to', 'date_from']


class global_sales_form(ModelForm):
    class Meta:
        model = global_sales_report
        fields = ['date_to', 'date_from']
