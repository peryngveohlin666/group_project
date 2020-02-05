from django.db import models
from django.contrib.auth.models import User

type_choices = (
        ('444', 'international up to four coupons'),
        ('440', 'manual - international'),
        ('420', 'international with two coupons'),
        ('201', 'domestic with two coupons'),
        ('101', 'domestic with one coupon'),
        ('451', 'MCO'),
        ('452', 'MCO'),
    )

class blank(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=50, choices=type_choices, default='green')
    is_sold = models.BooleanField(default=False)
    is_refunded = models.BooleanField(default=False)
    advisor = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )