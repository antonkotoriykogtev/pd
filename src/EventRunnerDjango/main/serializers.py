from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Event, CustomUser, User_in_Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id','name', 'start_date', 'end_date', 'picture_link','description','price','max_participants_quantity','address','geopoint_lat','geopoint_long','ics_file_link','is_online')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone_number','about_me','date_of_birth','picture_link','city','notification_type','data_visibility_type']

class User_in_EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_in_Event
        fields = ('id','user_id','event_id')