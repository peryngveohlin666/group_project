from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms


class register_form(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'group']

