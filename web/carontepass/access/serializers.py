from rest_framework import serializers
from carontepass.settings import VALUE_PAYMENT_TRUE
from .models import User, Device, Payment, Log
import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = ('id', 'name', 'rol')

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
            model = Device
            fields = ('id', 'user', 'kind', 'code')
            
            
class DeviceResultSerializer(serializers.ModelSerializer):
    
    result = serializers.SerializerMethodField('is_auth_user')
    
    def is_auth_user(self, Device):
        
        month_actual = datetime.datetime.now().month
        
        if Payment.objects.filter(user=Device.user, month=month_actual): 
            if  Payment.objects.filter(user=Device.user, month=month_actual)[0].amount >= VALUE_PAYMENT_TRUE:
                
                Log.checkentryLog(Device)
                
                return True;
            
        
    
    class Meta:
            model = Device
            fields = ('id', 'user', 'kind', 'code', 'result')
            