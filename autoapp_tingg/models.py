from django.db import models
from django.shortcuts import reverse


# Create your models here.


class APISettings(models.Model):
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
    display_name = models.CharField(max_length=30)
    unique_name = models.CharField(max_length=50)
    url = models.URLField()
    environment = models.CharField(max_length=20)
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
    display_name = models.CharField(max_length=50)
    unique_name = models.CharField(max_length=50)
    url = models.URLField()
    path = models.CharField(max_length=20)
    environment = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.display_name

    class Meta:
        verbose_name = 'UI Setting'
        verbose_name_plural = 'UI Settings'
        db_table = 'UISettings'


class JSONSimulator(models.Model):
    ACCEPT = '1'
    REJECT = '2'
    CHOICES = [
        (ACCEPT, 'Active'),
        (REJECT, 'In-active'),
    ]
    status = models.CharField(max_length=2,
                              choices=CHOICES,
                              default=REJECT
                              )
    unique_name = models.CharField(max_length=10)
    url = models.URLField()
    path = models.CharField(max_length=50)
    environment = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.unique_name

    class Meta:
        verbose_name = 'JSONSimulator'
        verbose_name_plural = 'JSONSimulators'
        db_table = 'JSONSimulator'


class MockingData(models.Model):
    ACTIVE = '1'
    INACTIVE = '2'
    CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'In-active'),
    ]
    status = models.CharField(max_length=2,
                              choices=CHOICES,
                              default=INACTIVE,
                              )
    unique_name = models.CharField(max_length=10, unique=True)

    json_string = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name = 'Mocking Data'
        verbose_name_plural = 'Mocking Data'
        db_table = 'MockingData'


class TestrailDetails(models.Model):
    ACTIVE = '1'
    INACTIVE = '2'
    CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'In-active'),
    ]
    status = models.CharField(max_length=2,
                              choices=CHOICES,
                              default=INACTIVE,
                              )
    testrail_username = models.CharField(max_length=200)
    testrail_password = models.CharField(max_length=200)
    testrail_url = models.URLField()

    class Meta:
        verbose_name = 'TestRail'
        verbose_name_plural = 'TestRail Settings'
        db_table = 'TestRail'
