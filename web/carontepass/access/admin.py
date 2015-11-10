from django.contrib import admin

from access.models import Group, User, Message, Payment, Device, Log

class UserAdmin(admin.ModelAdmin): 
  list_display = ('name', 'last_name', 'email', 'rol') 
  search_fields = ('name', 'last_name', 'email')
  list_filter = ('rol',) 
  
class DeviceAdmin(admin.ModelAdmin): 
  list_display = ('kind', 'user', 'code') 
  search_fields = ('user', 'code')
  list_filter = ('kind',) 
  
class LogAdmin(admin.ModelAdmin): 
  list_display = ('user', 'ts_input', 'ts_output') 
  search_fields = ('user', 'ts_input', 'ts_output')
  list_filter = ('ts_input',)

class PaymentAdmin(admin.ModelAdmin): 
  list_display = ('user', 'month', 'year', 'f_payment', 'amount') 
  search_fields = ('user', 'month', 'year') 
  list_filter = ('month',)


# Register your models here.
admin.site.register(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Message)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Log, LogAdmin)