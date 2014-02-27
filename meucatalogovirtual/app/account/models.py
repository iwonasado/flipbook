# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.validators import MaxLengthValidator

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    descricao = models.TextField('Descrição', blank=True,validators=[MaxLengthValidator(250)])
    foto = models.FileField('Foto', blank=True, upload_to=getattr(settings, 'ACCOUNT_UPLOAD_TO', 'uploads/account'),help_text=_('Used for Avatar.'))


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
