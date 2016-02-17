from django.shortcuts import render
from rest_framework import generics
from .models import Device, Log
from .serializers import DeviceResultSerializer
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

class DeviceIDList(generics.ListAPIView):

    serializer_class = DeviceResultSerializer

    def get_queryset(self, **kwargs):

        code_id = self.kwargs['code']
        
        #Device.check_exists_device(code_id)
        
        return Device.objects.filter(code=code_id)
        
        
@login_required(login_url='/')
def homepage(request):
    users_count = User.objects.count()
    users_in_count = Log.listUsersCount()
    return render(request, 'access/index.html', {'users_count': users_count, 'users_in_count': users_in_count})
    

@login_required(login_url='/')    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/')
def personal_info(request):
    return render(request, 'access/info.html')


@login_required(login_url='/')
def device_info(request):
    device_list_user = Device.objects.filter(user=User).all()
    return render(request, 'access/devicelist.html', {'device_list_user': device_list_user})
    
    
    
    
    
    
    
    