from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.character.models import User, Skill


class Habit(models.Model):
    MONTHLY = 'monthly'
    WEEKLY = 'weekly'
    DAILY = 'daily'

    FREQUENCY_OPTIONS = (
        (MONTHLY, _('Monthly')),
        (WEEKLY, _('Weekly')),
        (DAILY, _('Daily')),
    )

    DAYS_CHOICES = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    )

    user = models.ForeignKey(User, related_name='habits', on_delete=models.CASCADE)
    name = models.CharField(max_length=140, null=False, blank=False)
    description = models.TextField(blank=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_OPTIONS, default=DAILY)
    run_at = models.PositiveIntegerField()  # Run every...
    week_day = models.CharField(choices=DAYS_CHOICES, max_length=20)  # If frequency is weekly the day it will run
    exp = models.PositiveIntegerField()

    # Calc Fields. These fields are made by previous calcs but they are stored to avoid recalculating every time
    number_of_day = models.PositiveIntegerField()


class Record(models.Model):
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE, related_name='records')
    date = models.DateField()
    note = models.CharField(max_length=250)
