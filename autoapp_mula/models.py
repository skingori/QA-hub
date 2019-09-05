from django.db import models
from django.shortcuts import reverse

# Create your models here.


class APISettings(models.Model):
    display_name = models.CharField(max_length=30)
    unique_name = models.CharField(max_length=10)
    url = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.display_name

    class Meta:
        verbose_name = 'Endpoint'
        verbose_name_plural = 'Endpoints'
        db_table = 'APISettings'
