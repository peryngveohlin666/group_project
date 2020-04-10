from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# models are database tables basically and you can instantiate them

# a table of types
type_choices = (
    ('444', '444 - International up to four coupons'),
    ('440', '440 - Manually Entered International'),
    ('420', '420 - International up to two coupons'),
    ('201', '201 - Domestic up to two coupons'),
    ('101', '101 - Domestic with one coupon'),
    ('451', '451 - Miscellaneous Charges Order (MCO)'),
    ('452', '452 - Miscellaneous Charges Order (MCO)'),
)

report_types = (
    ('Interline', 'Interline'),
    ('Domestic', 'Domestic'),
)


# a class to generate an object model of currency information with different values stored inside
class currency(models.Model):
    type = models.CharField(max_length=50, primary_key=True)
    rate = models.IntegerField(blank=False, null=False)
    count_420 = models.IntegerField(blank=True, null=True)
    count_444 = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)


# a class to generate an object model of card information with different values stored inside
class card(models.Model):
    number = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.TextField()


# a class to generate an object model of customer with different values stored inside
class customer(models.Model):
    is_regular = models.BooleanField(default=False)
    is_valued = models.BooleanField(default=False)
    name = models.CharField(max_length=50, primary_key=True)
    address = models.TextField()
    card_info = models.ManyToManyField(to=card, blank=True, null=True)


# a class to generate an object model of blank with different values stored inside
class blank(models.Model):
    # an integer field that automatically increments by itself as the object are created
    number = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, choices=type_choices, default='444')
    is_sold = models.BooleanField(default=False)
    is_refunded = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    price = models.IntegerField()
    discount = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    date_sale = models.DateField(blank=True, null=True)
    payment_due = models.DateField(auto_now_add=False, blank=True, null=True)
    commission_rate = models.IntegerField(blank=True, null=True)
    paid_by_card = models.BooleanField(default=False)
    advisor = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True
    )
    blank_customer = models.ForeignKey(
        customer,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    blank_currency = models.ForeignKey(
        currency,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    blank_card = models.ForeignKey(
        card,
        models.SET_NULL,
        blank=True,
        null=True,
    )


# a class to generate an object model of assigned range of blanks with different values stored inside
class assigned_range(models.Model):
    range_from = models.IntegerField()
    range_to = models.IntegerField()
    agent = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    date = models.DateField(auto_now_add=False, blank=True, null=True)
    sold_blank_count = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=50, choices=type_choices, default='None')


# a class to generate an object model of created of blanks with different values stored inside
class created_range(models.Model):
    range_from = models.IntegerField()
    range_to = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=50, choices=type_choices, default='None')


# a class to generate a stock turnover report
class stock_turnover_report(models.Model):
    date_from = models.DateField(auto_now_add=False)
    date_to = models.DateField(auto_now_add=False)
    assigned_range = models.ManyToManyField(to=assigned_range, blank=True, null=True)
    created_range = models.ManyToManyField(to=created_range, blank=True, null=True)
    blanks = models.ManyToManyField(to=blank, blank=True, null=True)


# a class to generate an individual sales report
class individual_sales_report(models.Model):
    agent = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    date_from = models.DateField(auto_now_add=False)
    date_to = models.DateField(auto_now_add=False)
    type = models.CharField(max_length=50, choices=report_types, default='Interline')


# a class to generate a global sales report
class global_sales_report(models.Model):
    date_from = models.DateField(auto_now_add=False)
    date_to = models.DateField(auto_now_add=False)
    type = models.CharField(max_length=50, choices=report_types, default='Interline')


# a class to generate a gbp report
class gbp_report(models.Model):
    date_from = models.DateField(auto_now_add=False)
    date_to = models.DateField(auto_now_add=False)