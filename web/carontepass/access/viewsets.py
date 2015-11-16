from rest_framework import viewsets

from .models import User, Device
from .serializers import UserSerializer, DeviceSerializer

 
class UserViewSet(viewsets.ModelViewSet):
 
    serializer_class = UserSerializer
    queryset = User.objects.all()


class DeviceViewSet(viewsets.ModelViewSet):
 
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()