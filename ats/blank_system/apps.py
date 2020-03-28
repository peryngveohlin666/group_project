from django.apps import AppConfig


class BlankSystemConfig(AppConfig):
    name = 'blank_system'

    def ready(self):
        # important do the import inside the method
        from django.contrib.auth.models import Group
        from django.contrib.auth.models import User

        Group.objects.get_or_create(name='system_administrator')
        Group.objects.get_or_create(name='manager')
        Group.objects.get_or_create(name='travel_advisor')
        user, created = User.objects.get_or_create(username='spike')
        user.set_password("mert123")
        user.save()
        spike = User.objects.get(username='spike')
        sysadmin = Group.objects.get(name='system_administrator')
        sysadmin.user_set.add(spike)
