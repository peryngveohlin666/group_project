from django.apps import AppConfig


class BlankSystemConfig(AppConfig):
    name = 'blank_system'

    def ready(self):
        # important do the import inside the method
        from django.contrib.auth.models import Group

        Group.objects.get_or_create(name='system_administrator')
        Group.objects.get_or_create(name='manager')
        Group.objects.get_or_create(name='travel_advisor')

        print("Test")