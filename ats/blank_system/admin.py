from django.contrib import admin
from .models import blank, customer, card, currency
# Register your models here.
admin.site.register(blank)
admin.site.register(customer)
admin.site.register(card)
admin.site.register(currency)
