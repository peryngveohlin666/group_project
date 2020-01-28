from django.contrib.auth.models import User, Group

main_sysadmin = User.objects.create(username='main_sysadmin', password='123456')

