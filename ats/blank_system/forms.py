from django.forms import ModelForm
from django import forms
from blank_system.models import blank, customer, card, currency, assigned_range


# a form object for blanks
class blank_form(ModelForm):
    class Meta:
        model = blank
        fields = ['type', 'is_sold', 'is_refunded', 'price']


class assign_blank_form(ModelForm):
    class Meta:
        model = blank
        fields = ['advisor', 'commission_rate']


class register_customer_form(ModelForm):
    class Meta:
        model = customer
        fields = ['is_regular', 'is_valued', 'name', 'address']


class register_card_form(ModelForm):
    class Meta:
        model = card
        fields = ['number', 'name', 'surname', 'address']


class sell_form(ModelForm):
    class Meta:
        model = blank
        fields = ['blank_customer', 'is_sold', 'is_paid', 'payment_due']


class add_currency_form(ModelForm):
    class Meta:
        model = currency
        fields = ['type', 'rate']