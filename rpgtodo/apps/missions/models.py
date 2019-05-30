from django.db import models

from django.contrib.auth.models import User

from apps.character.models import Skill


class Mission(models.Model):
    user = models.ForeignKey(User, related_name='missions', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.CharField(max_length=450, blank=True, default='')
    end_date = models.DateTimeField(null=True, blank=True)
    parent = models.ForeignKey('Mission', related_name='sub_missions', on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    complete_percentage = models.PositiveIntegerField(null=True)  # TODO field depending on submissions fields
    exp = models.PositiveIntegerField()


class SkillMission(models.Model):
    skill = models.ForeignKey('character.Skill', related_name='missions', on_delete=models.CASCADE)
    mission = models.ForeignKey('Mission', related_name='skills', on_delete=models.CASCADE)
    exp = models.PositiveIntegerField()
