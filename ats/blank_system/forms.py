from django.forms import ModelForm
from blank_system.models import blank

# a form object for blanks
class blank_form(ModelForm):
    class Meta:
        model = blank
        fields = ['type', 'is_sold', 'is_refunded']


class assign_blank_form(ModelForm):
    class Meta:
        model = blank
        fields = ['advisor']