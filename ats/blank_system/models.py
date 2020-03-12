from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# a table of types
type_choices = (
    ('444', 'international up to four coupons'),
    ('440', 'manual - international'),
    ('420', 'international with two coupons'),
    ('201', 'domestic with two coupons'),
    ('101', 'domestic with one coupon'),
    ('451', 'MCO - 451'),
    ('452', 'MCO - 452'),
)

# a class to generate an object model of currency information with different values stored inside
class currency(models.Model):
    type = models.CharField(max_length=50, primary_key=True)
    rate = models.IntegerField(blank=False, null=False)


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
    type = models.CharField(max_length=50, choices=type_choices, default='green')
    is_sold = models.BooleanField(default=False)
    is_refunded = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    payment_due = models.DateField(auto_now_add=False)
    commission_rate = models.IntegerField(blank=True, null=True)
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


class stock_turnover_report(models.Model):
    date_from = models.DateField(auto_now_add=False)
    date_to = models.DateField(auto_now_add=False)
    assigned_range = models.ManyToManyField(to=assigned_range, blank=True, null=True)
    blanks = models.ManyToManyField(to=blank, blank=True, null=True)