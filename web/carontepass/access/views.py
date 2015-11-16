from django.shortcuts import render
from rest_framework import generics
from .models import User, Device
from .serializers import UserSerializer, DeviceResultSerializer

# Create your views here.

class DeviceIDList(generics.ListAPIView):

    serializer_class = DeviceResultSerializer

    def get_queryset(self, **kwargs):

        code_id = self.kwargs['code']
        return Device.objects.filter(code=code_id)