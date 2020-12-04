from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from main.serializers import UserSerializer
from .models import Event, CustomUser
from .serializers import EventSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-start_date')
    serializer_class = EventSerializer
