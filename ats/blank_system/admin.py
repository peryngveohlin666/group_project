from django.contrib import admin
from .models import blank, customer, card, currency, assigned_range, stock_turnover_report, created_range, individual_sales_report
# Register your models here.
admin.site.register(blank)
admin.site.register(customer)
admin.site.register(card)
admin.site.register(currency)
admin.site.register(assigned_range)
admin.site.register(stock_turnover_report)
admin.site.register(created_range)
admin.site.register(individual_sales_report)