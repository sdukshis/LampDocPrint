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


class Brand(models.Model):
    name = models.CharField(verbose_name=_('Brand'), max_length=256)

    def __unicode__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(verbose_name=_('Series'), max_length=256)

    def __unicode__(self):
        return self.name


class Lamp(Changeable):
    E14 = 'E14'
    E27 = 'E27'
    R7S = 'R7S'
    G9 = 'G9'
    MR16 = 'MR16'
    SOCKET_TYPES = (
        (E14, E14),
        (E27, E27),
        (R7S, R7S),
        (G9, G9),
        (MR16, MR16),
    )

    F03 = '03'
    F04 = '04'
    F05 = '05'
    FLAMMABLE_TYPES = (
        (F03, 'Normal flammable surfaces'),
        (F04, 'Not on flammable surfaces'),
        (F05, 'May be covered'),
    )
    F06 = '06'
    F07 = '07'
    F08 = '08'
    FIXING_TYPES = (
        (F06, 'Ceiling'),
        (F07, 'Wall'),
        (F08, 'Wall and ceiling'),
    )
    D05 = 0.5
    D08 = 0.8
    D10 = 1.0
    DISTANCE_TYPES = (
        (D05, D05),
        (D08, D08),
        (D10, D10),
    )
    PC1 = '19'
    PC2 = '20'
    PC3 = '21'
    PROTECTION_TYPES = (
        (PC1, '19'),
        (PC2, '20'),
        (PC3, '21'),
    )
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='lamps/')
    brand = models.ForeignKey(Brand, verbose_name=_('Brand'))
    art = models.CharField(verbose_name=_('Article'), max_length=512)
    name = models.CharField(verbose_name=_('Name'), max_length=512)
    contractor = models.ForeignKey(Contractor, verbose_name=_('Contractor'))
    contractor_art = models.CharField(verbose_name=_('Contractor article'),
                                      max_length=512)
    series = models.ForeignKey(Series, verbose_name=_('Series'))
    material = models.CharField(verbose_name=_('Material'), max_length=512)
    color = models.CharField(verbose_name=_('Color'), max_length=512)
    barcode = models.CharField(verbose_name=_('Bar code'), max_length=512)
    construction = models.CharField(verbose_name=_('Construction'),
                                    max_length=512)
    diameter = models.PositiveIntegerField(verbose_name=_('Diameter'))
    height = models.PositiveIntegerField(verbose_name=_('Height'))
    width = models.PositiveIntegerField(verbose_name=_('Width'),
                                        blank=True,
                                        null=True)
    socket = models.CharField(verbose_name=_('Lampholder'),
                              choices=SOCKET_TYPES,
                              default=E14,
                              max_length=128)
    indoors = models.BooleanField(default=True)
    flammable = models.CharField(choices=FLAMMABLE_TYPES,
                                 default=F03,
                                 max_length=128)
    fixing = models.CharField(choices=FIXING_TYPES,
                              default=F06,
                              max_length=128)
    distance = models.FloatField(verbose_name=_('Minimum distance'),
                                 choices=DISTANCE_TYPES,
                                 default=D05)
    IPX1 = models.BooleanField(verbose_name=_('IPX1'), default=True)
    protection = models.CharField(verbose_name=_('Protection class'),
                                  choices=PROTECTION_TYPES,
                                  default=PC1,
                                  max_length=128)
    F36 = models.BooleanField(default=False)
    F37 = models.BooleanField(default=True)
    F39 = models.BooleanField(default=False)
    F51 = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('lamp_update', kwargs={'pk': self.pk})
