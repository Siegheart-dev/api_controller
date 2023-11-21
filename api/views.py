from django.shortcuts import render
from .models import Room
from rest_framework import generics
from .serializers import RoomSerializer
import requests


class Func(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


def ok(request):
    return render(request, 'OK')


