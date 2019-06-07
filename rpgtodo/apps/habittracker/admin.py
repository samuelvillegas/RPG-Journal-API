from django.contrib import admin

from apps.habittracker.models import Habit, Record


class RecordInline(admin.StackedInline):
    model = Record
    extra = 0


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'start_date', 'end_date', 'number_of_days')
    inlines = [
        RecordInline
    ]
