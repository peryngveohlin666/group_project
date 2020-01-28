from django.contrib.auth.models import User


sysadmin = User.objects.create(username='sysadmin', password='123456')
sysadmin.save()
