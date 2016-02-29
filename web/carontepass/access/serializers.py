from rest_framework import serializers
from carontepass.settings import VALUE_PAYMENT_TRUE, MAX_GRANTED_DAYS
from .models import Device, Payment, Log, Message
import datetime
from django.contrib.auth.models import User

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
        
        #Check if the user has monthly payments
        month_actual = datetime.datetime.now().month
        
        if Payment.objects.filter(user=Device.user, month=month_actual): 
            if  Payment.objects.filter(user=Device.user, month=month_actual)[0].amount >= VALUE_PAYMENT_TRUE:
                
                Log.checkentryLog(Device)
                Message.message_detect_tag(Device)
                return True;
        
        
        #Grace period for the first day of the month
        if not Device.kind == "tag":
            #The tags that have no assigned user are exempt from the days of courtesy.
            day_actual = datetime.datetime.now().day
            
            if datetime.datetime.now().day <= MAX_GRANTED_DAYS:
                
                Log.checkentryLog(Device)
                Message.message_detect_tag(Device)
                return True;
                
    class Meta:
            model = Device
            fields = ('id', 'user', 'kind', 'code', 'result')
            
    