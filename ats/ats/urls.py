from django.contrib import admin
from django.urls import path
from .views import index, homepage
from blank_system.views import create_blanks, blanks, assign_blanks, register_customer
#url patterns for the pages we use in views.py so that we won't have to write the whole directory tree


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='index'),
    path('homepage', homepage, name='homepage'),
    path('create_blanks', create_blanks, name='create_blanks'),
    path('blanks', blanks, name='blanks'),
    path('assign_blanks', assign_blanks, name='assign_blanks'),
    path('register_customer', register_customer, name='register_customer')
]
