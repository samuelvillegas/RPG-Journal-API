from django.contrib import admin

from apps.missions.models import Mission


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'parent', 'is_complete', 'exp')


