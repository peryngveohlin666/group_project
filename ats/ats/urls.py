from django.contrib import admin
from django.urls import path
from .views import index, homepage, register_user, logout_view
from blank_system.views import create_blanks, blanks, assign_blanks, register_customer, my_blanks, register_card, blanku_by_card, blanku_by_cash, add_currency, create_stock_turnover_report, view_stock_turnover_report
#url patterns for the pages we use in views.py so that we won't have to write the whole directory tree

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='index'),
    path('homepage', homepage, name='homepage'),
    path('create_blanks', create_blanks, name='create_blanks'),
    path('blanks', blanks, name='blanks'),
    path('assign_blanks', assign_blanks, name='assign_blanks'),
    path('register_customer', register_customer, name='register_customer'),
    path('register_user', register_user, name='register_user'),
    path('my_blanks', my_blanks, name='my_blanks'),
    path('register_card', register_card , name='register_card'),
    path('blanku_by_card/<int:number>/', blanku_by_card, name='blanku_by_card'),
    path('blanku_by_cash/<int:number>/', blanku_by_cash, name='blanku_by_cash'),
    path('add_currency', add_currency, name='add_currency'),
    path('logout', logout_view, name='logout_view'),
    path('create_stock_turnover_report', create_stock_turnover_report, name='create_stock_turnover_report'),
    path('view_stock_turnover_report/<int:number>/', view_stock_turnover_report, name='view_stock_turnover_report')
]
