from django.forms import ModelForm
from django import forms
from blank_system.models import blank, customer, card, currency, assigned_range, stock_turnover_report, individual_sales_report, global_sales_report, gbp_report

# these are all form objects that generate html forms automatically for you, it is just a lazy django alternative to html forms and dealing with each box one by one

# a form object for blanks
class blank_form(ModelForm):
    class Meta:
        #the model the form references to
        model = blank
        #the fields to fill in the form for that model
        fields = ['type', 'price']


# a form to support assigning blanks
class assign_blank_form(ModelForm):
    class Meta:
        # the model the form references to
        model = blank
        # the fields to fill in the form for that model
        fields = ['advisor', 'commission_rate']


# a form to register customers
class register_customer_form(ModelForm):
    class Meta:
        # the model the form references to
        model = customer
        # the fields to fill in the form for that model
        fields = ['is_regular', 'is_valued', 'name', 'address']


# a form object for card
class register_card_form(ModelForm):
    class Meta:
        model = card
        fields = ['number', 'name', 'surname', 'address']


# a form object for sales
class sell_form(ModelForm):
    class Meta:
        model = blank
        fields = ['blank_customer', 'is_paid', 'blank_currency', 'discount']


# a form object for currencies
class add_currency_form(ModelForm):
    class Meta:
        model = currency
        fields = ['type', 'rate']


# a form object for stock turnover reports
class stock_turnover_form(ModelForm):
    class Meta:
        model = stock_turnover_report
        fields = ['date_to', 'date_from']


# a form object for individual sales reports (manager)
class individual_sales_form_manager(ModelForm):
    class Meta:
        model = individual_sales_report
        fields = ['date_to', 'date_from', 'agent', 'type']


# a form object for individual sales reports (agent)
class individual_sales_form_agent(ModelForm):
    class Meta:
        model = individual_sales_report
        fields = ['date_to', 'date_from', 'type']


# a form  object for the global sales form
class global_sales_form(ModelForm):
    class Meta:
        model = global_sales_report
        fields = ['date_to', 'date_from', 'type']


# a form object for the gbp forms
class gbp_report_form(ModelForm):
    class Meta:
        model = gbp_report
        fields = ['date_from', 'date_to']
