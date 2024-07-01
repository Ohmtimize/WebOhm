from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID
from django.contrib.auth.models import BaseUserManager, AbstractUser, Group, Permission

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field

#from phonenumber_field.modelfields import PhoneNumberField

class Installation(models.Model):
    """Model representing a client's installation."""

    address = models.CharField(
        max_length=200,
        unique=True,
        help_text='Enter installation address'
    )

    postcode = models.CharField(max_length=4, help_text='Enter postcode', default='0000')

    date = models.DateField(null=True, blank=True)

    def __str__(self):
        """String for representing the Installation object (in Admin site etc.)."""
        return self.address
    

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of Installation."""
        return reverse('installation-detail', args=[str(self.id)])
    
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('address'),
                name='installation_address_case_insensitive_unique',
                violation_error_message='An installation with that address already exists.'
            ),
        ]

class Client(models.Model):
    """Model representing a client."""

    STARTER = "ST"
    ADVANCED = "AD"
    MEMBER_TYPES = [
        (STARTER, "Starter"),
        (ADVANCED, "Advanced"),
    ]

    customerNumber = models.CharField(
        max_length=200,
        unique=True,
        help_text='Enter customer number'
    )

    memberType = models.CharField(max_length=2, choices=MEMBER_TYPES, default=STARTER, help_text='Enter member type')

    def __str__(self):
        """String for representing the Client object."""
        return self.customerNumber
    
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of Client."""
        return reverse('client-detail', args=[str(self.id)])


class Billing(models.Model):
    """Model representing a billing."""

    paid = models.BooleanField(default=False, help_text='Paid?')
    date = models.DateTimeField(auto_now_add=True)
    billingDetails = models.CharField(max_length=300, help_text='Billing details')

    def __str__(self):
        """String for representing the Billing object."""
        return str(self.paid)

class SolarPanel(models.Model):
    """Model representing a solar panel."""

    panelType = models.CharField(max_length=100, help_text='Enter panel type')
    brand = models.CharField(max_length=100, help_text='Enter panel brand')
    maxPower = models.DecimalField(max_digits=5, decimal_places=2, help_text='Enter panel max power')
    orientation = models.CharField(max_length=100, help_text='Enter panel orientation')
    year = models.IntegerField(help_text='Enter panel year')

    def __str__(self):
        """String for representing the SolarPanel object."""
        return self.panelType   
    

class Device(models.Model):
    """Model representing a device."""

    DEVICE_STATUS = [
        ('ON', 'ON'),
        ('OFF', 'OFF'),
        ('UNKNOWN', 'UNKNOWN'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, help_text='Enter device name <br><br>')
    value = models.FloatField(help_text='Enter device value <br><br>', default=0)
    units = models.CharField(max_length=10, help_text='Enter device units <br><br>')
    dateTime = models.DateTimeField(auto_now_add=timezone.now)
    deviceStatus = models.CharField(max_length=7, choices=DEVICE_STATUS, default='UNKNOWN', help_text='Enter device status <br><br>')

    def __str__(self):
        """String for representing the Device object."""
        return self.name


class Consumption(models.Model):
    """Model representing a customer's consumption."""
    consumption = models.FloatField(help_text='Enter consumption')
    dateTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

class Production(models.Model):
    """Model representing a customer's production."""
    production = models.FloatField(help_text='Enter production')
    dateTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

class GridExchange(models.Model):
    """Model representing a customer's grid exchange."""
    gridExchange = models.FloatField(help_text='Enter grid exchange value')
    dateTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)