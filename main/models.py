# -*- encoding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Changeable(models.Model):
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)


class Contractor(Changeable):
    name_eng = models.CharField(verbose_name=u'Название фабрики (англ.)',
                                     max_length=256)
    address_eng = models.CharField(verbose_name=u'Адрес (англ.)',
                                     max_length=512)
    name_rus = models.CharField(verbose_name=u'Название (рус.)',
                                     max_length=256)
    address_rus = models.CharField(verbose_name=u'Адрес (рус.)',
                                     max_length=512)
    logo = models.ImageField(verbose_name=u'Логотип', upload_to='logo/')

    def __unicode__(self):
        return self.name_eng
        
    def get_absolute_url(self):
        return reverse('contractor_update', kwargs={'pk': self.pk})
