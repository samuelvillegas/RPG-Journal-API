from django.contrib import admin

from apps.character.models import Character, Skill


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'exp')
