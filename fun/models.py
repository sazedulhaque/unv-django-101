from django.db import models

# Create your models here.


class Fun(models.Model):
    fun_fact = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
