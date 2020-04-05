from django.contrib.auth.models import User, Group
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class register_form(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'group']


class AuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.error_messages = {
            'invalid_login': (
                "The details entered are incorrect, please try again."
            ),
            'inactive': ("This account is inactive."),
        }

        for field in self.fields.values():
            field.error_messages = {'required': '{fieldname} is required'.format(
                fieldname=field.label)}
