from django.contrib.auth.models import Group, Permission

#a script to initialize groups, we are going to add permissions here afterwise
def initialize():
    system_administrator = Group.objects.get_or_create(name='system_administrator')
    manager = Group.objects.get_or_create(name='manager')
    travel_advisor = Group.objects.get_or_create(name='travel_advisor')

