from django.shortcuts import render
from rest_framework import generics
from .models import Device, Log
from .serializers import DeviceResultSerializer
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.

class DeviceIDList(generics.ListAPIView):

    serializer_class = DeviceResultSerializer

    def get_queryset(self, **kwargs):

        code_id = self.kwargs['code']
        
        #Device.check_exists_device(code_id)
        
        return Device.objects.filter(code=code_id)
        

def homepage(request):
    users_count = User.objects.count()
    users_in_count = Log.listUsersCount()
    return render(request, 'access/index.html', {'users_count': users_count, 'users_in_count': users_in_count})
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
    