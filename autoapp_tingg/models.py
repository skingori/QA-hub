from django.db import models
from django.shortcuts import reverse


# Create your models here.


class APISettings(models.Model):
    display_name = models.CharField(max_length=30)
    unique_name = models.CharField(max_length=50, unique=True)
    url = models.URLField()
    port = models.IntegerField()
    path = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.display_name

    class Meta:
        verbose_name = 'Endpoint'
        verbose_name_plural = 'Endpoints'
        db_table = 'APISettings'


class WebHook(models.Model):
    ACCEPT = '1'
    REJECT = '2'
    CHOICES = [
        (ACCEPT, 'Active'),
        (REJECT, 'In-active'),
    ]
    status = models.CharField(max_length=2,
                              choices=CHOICES,
                              default=REJECT,
                              )
    status_code = models.CharField(max_length=3)
    url = models.URLField()
    fail_url = models.URLField()
    success_url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.status_code

    class Meta:
        verbose_name = 'WebHook'
        verbose_name_plural = 'WebHooks'
        db_table = 'WebHookSettings'


class UISettings(models.Model):
    display_name = models.CharField(max_length=50)
    unique_name = models.CharField(max_length=50, unique=True)
    encoded_url = models.URLField()
    url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.display_name

    class Meta:
        verbose_name = 'UI Setting'
        verbose_name_plural = 'UI Settings'
        db_table = 'UISettings'


class EnvironmentPorts(models.Model):
    display_name = models.CharField(max_length=20)
    unique_name = models.CharField(max_length=10, unique=True)
    port = models.CharField(max_length=6)
    description = models.TextField()

    def __str__(self):
        return self.display_name

    class Meta:
        verbose_name = 'Environment'
        verbose_name_plural = 'Environment'
        db_table = 'Environment'


class JSONSimulator(models.Model):
    unique_name = models.CharField(max_length=10, unique=True)

    url = models.URLField()
    description = models.TextField()
