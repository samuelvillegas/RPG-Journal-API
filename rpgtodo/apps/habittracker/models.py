import datetime

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
    description = models.TextField(blank=True, default='')
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_OPTIONS, default=DAILY)
    run_at = models.PositiveIntegerField(null=True)  # Run every...
    week_day = models.CharField(choices=DAYS_CHOICES, max_length=20, default='monday') # If frequency is weekly the day it will run
    exp = models.PositiveIntegerField(default=0)

    # Calc Fields. These fields are made by previous calcs but they are stored to avoid recalculating every time
    number_of_days = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        delta = self.end_date - self.start_date
        if delta.days < 0:
            self.number_of_days = 0
        else:
            self.number_of_days = delta.days
        super(Habit, self).save(*args, **kwargs)

    def longest_streak(self, entry_dates):
        longest_streak = 0
        chain = 0

        if len(entry_dates) <= 0:
            return 0

        longest_compare_date = entry_dates[0]['date']
        for date in entry_dates:
            # Calc longest streak
            longest_delta = longest_compare_date - date['date']
            if longest_delta.days == 1:
                chain += 1
            else:
                chain = 1

            if chain > longest_streak:
                longest_streak = chain

            longest_compare_date = date['date']

        return longest_streak

    def current_streak(self, entry_dates):
        total_streak = 0
        current_streak = 0
        today = datetime.date.today()
        compare_date = today + datetime.timedelta(1)  # Tomorrow
        for date in entry_dates:
            # Calc Current streak
            # Get the difference btw the dates
            delta = compare_date - date['date']

            if delta.days == 1:  # Keep the streak going!
                current_streak += 1
            elif delta.days == 0:  # Don't bother increasing the day if there's multiple ones on the same day
                pass
            else:  # Awwww...
                break  # The current streak is done, exit the loop

            compare_date = date['date']

        if current_streak > total_streak:
            total_streak = current_streak

        return total_streak

    def calc_streaks(self):
        today = datetime.date.today()

        entry_dates = list(Record.objects.values("date").filter(habit=self, date__lte=today).order_by("-date"))

        longest_streak = self.longest_streak(entry_dates)
        current_streak = self.current_streak(entry_dates)

        return {
            'current_streak': current_streak,
            'longest_streak': longest_streak
        }


class Record(models.Model):
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE, related_name='records')
    date = models.DateField()
    note = models.CharField(max_length=250, blank=True)

    class Meta:
        unique_together = ('habit', 'date',)
