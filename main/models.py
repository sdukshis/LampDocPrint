# -*- encoding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
# Create your models here.

class Changeable(models.Model):
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)


class Contractor(Changeable):
    name_eng = models.CharField(verbose_name=_('Name (eng.)'),
                                     max_length=256)
    address_eng = models.CharField(verbose_name=_('Address (eng.)'),
                                     max_length=512)
    name_rus = models.CharField(verbose_name=_('Name (rus.)'),
                                     max_length=256)
    address_rus = models.CharField(verbose_name=_('Address (rus.)'),
                                     max_length=512)
    logo = models.ImageField(verbose_name=_('Logo'), upload_to='logo/')

    def __unicode__(self):
        return self.name_eng
        
    def get_absolute_url(self):
        return reverse('contractor_update', kwargs={'pk': self.pk})
