import datetime

from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    user = models.CharField(max_length=30,blank=True,default=0)
    email = models.CharField(max_length=30,blank=True,default=0)
    senha = models.CharField(max_length=30,blank=True,default=0)
    mensagem = models.TextField(max_length=30,blank=True,default=0)
    contato = models.IntegerField(blank=True,default=0)

