from django.db import models

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User


def upload_user_avatar(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    return "users/{id}/{name}{ext}".format(id=instance.pk, name=fn, ext=ext)


class Character(models.Model):
    user = models.OneToOneField(User, related_name='character', on_delete=models.CASCADE, verbose_name=_('User'))
    picture = models.ImageField(verbose_name=_('Avatar'), null=True, blank=True, upload_to=upload_user_avatar)


class Skill(models.Model):
    user = models.ForeignKey(User, related_name='skills', on_delete=models.CASCADE)
    level = models.PositiveIntegerField()
    exp = models.PositiveIntegerField()


