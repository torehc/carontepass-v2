from rest_framework import serializers
from .models import User, Device


class UserSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = ('id', 'name', 'rol')

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
            model = Device
            fields = ('id', 'user', 'kind', 'code')
