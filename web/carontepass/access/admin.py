from django.contrib import admin

from access.models import Message, Payment, Device, Log, Telegram


class DeviceAdmin(admin.ModelAdmin): 
  list_display = ('kind', 'user', 'code') 
  search_fields = ('user', 'code')
  list_filter = ('kind',) 
  
class LogAdmin(admin.ModelAdmin): 
  list_display = ('user', 'ts_input', 'ts_output', 'day', 'user_in') 
  search_fields = ('user', 'ts_input', 'ts_output')
  list_filter = ('ts_input', 'user_in')
  
  def day(self, obj):
    return obj.ts_input.strftime('%A')

class PaymentAdmin(admin.ModelAdmin): 
  list_display = ('user', 'month', 'year', 'f_payment', 'amount') 
  search_fields = ('user', 'month', 'year') 
  list_filter = ('month',)
  
class MessageAdmin(admin.ModelAdmin): 
  list_display = ('rol', 'text')
  list_filter = ('rol',)
  
class TelegramAdmin(admin.ModelAdmin): 
  list_display = ('user', 'chatid') 
  search_fields = ('user', 'chatid') 


# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Telegram, TelegramAdmin)