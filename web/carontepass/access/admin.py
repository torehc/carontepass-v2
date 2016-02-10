from django.contrib import admin

from access.models import Message, Payment, Device, Log


class DeviceAdmin(admin.ModelAdmin): 
  list_display = ('kind', 'user', 'code') 
  search_fields = ('user', 'code')
  list_filter = ('kind',) 
  
class LogAdmin(admin.ModelAdmin): 
  list_display = ('user', 'ts_input', 'ts_output', 'user_in') 
  search_fields = ('user', 'ts_input', 'ts_output')
  list_filter = ('ts_input', 'user_in')

class PaymentAdmin(admin.ModelAdmin): 
  list_display = ('user', 'month', 'year', 'f_payment', 'amount') 
  search_fields = ('user', 'month', 'year') 
  list_filter = ('month',)
  
class MessageAdmin(admin.ModelAdmin): 
  list_display = ('rol', 'text')
  list_filter = ('rol',)


# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Log, LogAdmin)