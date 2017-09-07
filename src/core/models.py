from __future__ import unicode_literals
import csv
import io
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify

from .signals import csv_uploaded
from .validators import csv_file_validator


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Distrito(TimeStampedModel):
    cod_distrito = models.AutoField(max_length=10, primary_key=True)
    des_distrito = models.CharField(max_length=200)

    def __str__(self):  # __unicode__ on Python 2
        return self.des_distrito


class SubPrefeitura(TimeStampedModel):
    cod_subprefeitura = models.AutoField(max_length=10, primary_key=True)
    des_subprefeitura = models.CharField(max_length=200)

    def __str__(self):  # __unicode__ on Python 2
        return self.des_subprefeitura


class Feira(TimeStampedModel):
    REGIAO5_CHOICES = (
        ('1', 'Leste'),
        ('2', 'Oeste'),
        ('3', 'Norte'),
        ('4', 'Centro'),
        ('5', 'Sul'),
    )

    REGIAO8_CHOICES = (
        ('1', 'Leste 1'),
        ('2', 'Oeste'),
        ('3', 'Norte 1'),
        ('4', 'Centro'),
        ('5', 'Sul 1'),
        ('6', 'Sul 2'),
    )
    id = models.AutoField(primary_key=True)
    long = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    setcens = models.CharField(max_length=100)
    areap = models.CharField(max_length=100)
    coddist = models.ForeignKey(Distrito)
    codsubpref = models.ForeignKey(SubPrefeitura)
    regiao5 = models.CharField(max_length=1, choices=REGIAO5_CHOICES)
    regiao8 = models.CharField(max_length=1, choices=REGIAO8_CHOICES)
    nome_feira = models.CharField(max_length=200)
    registro = models.CharField(max_length=200)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    referencia = models.CharField(max_length=200)

    def __str__(self):  # __unicode__ on Python 2
        return self.nome_feira
