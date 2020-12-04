from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    phone_number = models.CharField(max_length=20, blank=True)
    about_me = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True)
    picture_link = models.ImageField(upload_to='media', max_length=254, default=" ", blank=True)
    city = models.CharField(max_length=50, blank=True)
    notification_type = models.IntegerField(null=True)
    data_visibility_type = models.IntegerField(null=True)


    def __str__(self):
        return self.email

class Event(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    picture_link = models.ImageField(blank=True, upload_to='media', max_length=254, default=" ",)
    description = models.TextField(blank=True)
    price = models.FloatField(null=True)
    max_participants_quantity = models.IntegerField(null=True)
    address = models.CharField(max_length=255, blank=True)
    geopoint_lat = models.FloatField(null=True)
    geopoint_long = models.FloatField(null=True)
    ics_file_link = models.FileField(null=True)    
    is_online = models.BooleanField(default=0)

class User_in_Event(models.Model):
    user_id = models.ForeignKey('CustomUser', on_delete=models.SET(0))
    event_id = models.ForeignKey('Event', on_delete=models.SET(0))
