from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'groups', 'first_name', 'last_name', 'email']
