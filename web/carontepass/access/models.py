# -*- encoding: utf-8 -*-
from django.db import models
import datetime
from telegram_group import send_group_msg


# Create your models here.
class Group(models.Model):
    __tablename__ = 'cp_group'

    name_group = models.CharField(max_length=50)
    url = models.CharField(max_length=160, verbose_name='Url Web')
    
    def __str__(self):
        return self.name_group


class User(models.Model):
    __tablename__ = 'cp_user'
    
    USER = 'USER'
    ADMI = 'ADMI'
    ROL_CHOICES = (
        (USER, 'User'),
        (ADMI, 'Administrator'),
    )
    
    name = models.CharField(max_length=60, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    
    rol = models.CharField(max_length=4,
                                      choices=ROL_CHOICES,
                                      default=USER,
                                      blank=False,
                                      )
    
    group = models.ForeignKey('Group')
    phone = models.CharField(max_length=18, blank=False)
    address = models.CharField(max_length=220)
    email = models.CharField(max_length=180, blank=False)
    
    
    def full_name(self):
        return '{} {}'.format(self.name, self.last_name)

    def __str__(self):
        return u'{} {}'.format(self.name, self.last_name)


class Message(models.Model):
    __tablename__ = 'cp_message'
    
    INPUT = 'Input'
    OUTPUT = 'Output'
    CAUTION = 'Caution'
    INFO = 'Info'
    
    ROL_CHOICES = (
        (INPUT, 'Input'),
        (OUTPUT, 'Output'),
        (CAUTION, 'Caution'),
        (INFO, 'Info'),
    )
    
    text = models.CharField(max_length=512)
    
    rol = models.CharField(max_length=7,
                                      choices=ROL_CHOICES,
                                      default=INFO,
                                      blank=False,
                                      )


class Payment(models.Model):
    __tablename__ = 'cp_payment'

    year = models.IntegerField()
    month = models.IntegerField()
    user = models.ForeignKey('User')
    f_payment = models.DateTimeField()
    amount = models.FloatField(default=0.0)
    
    def __str__(self):
        return '{}: {} - {}'.format(self.user, self.amount, self.f_payment)
        

class Device(models.Model):
    __tablename__ = 'cp_device'
    
    NFC = 'nfc'
    MAC = 'mac'
    DEVICE_CHOICES = (
        (NFC, 'NFC'),
        (MAC, 'MAC'),
    )

    user = models.ForeignKey('User')
    kind = models.CharField(max_length=3,
                                      choices=DEVICE_CHOICES,
                                      default=NFC,
                                      blank=False,
                                      )
    code = models.CharField(max_length=64, blank=False)
    
    def __str__(self):
        return 'Device {}:{} - {}'.format(self.user, self.kind, self.code)


class Log(models.Model):
    __tablename__ = 'cp_log'

    user = models.ForeignKey('User')
    ts_input = models.DateTimeField()
    ts_output = models.DateTimeField()
    user_in = models.BooleanField(default=False)
    
    def __str__(self):
        return 'Log {}: {} - {}'.format(self.user, self.ts_input, self.ts_output)
    
    @staticmethod   
    def checkentryLog(Device):

        date = datetime.datetime.now()

        log_obj = Log.objects.filter(user=Device.user).last()
        
        log_user_in_initial = len(Log.objects.filter(user_in=True).all())

        if not log_obj:

            log_create = Log.objects.create(user=Device.user, ts_input=date, ts_output=date, user_in=True)
            #return '{}: Go In'.format(device_obj.user)
            
        elif(log_obj.ts_input.strftime('%d/%m/%y-%H:%M') == log_obj.ts_output.strftime('%d/%m/%y-%H:%M')):
                    
            log_obj.ts_output = datetime.datetime.now()
            log_obj.user_in = False
            log_obj.save()
            #return '{}: Go Out'.format(device_obj.user)

        else:
            log_create = Log.objects.create(user=Device.user, ts_input=date, ts_output=date, user_in=True)    
            #return '{}: Go In'.format(device_obj.user)
     
        log_user_in_end = len(Log.objects.filter(user_in=True).all())
        
        
        if(log_user_in_initial == 0 and log_user_in_end == 1):
            send_group_msg(True, str(Device.user.name))
            
        elif(log_user_in_initial == 1 and log_user_in_end == 0):
            send_group_msg(False, str(Device.user.name))
           
            
    @staticmethod   
    def listUsersInside(self):
        
        logs_in = Log.objects.filter(user_in=True).all()
        return logs_in
        """
        for i in range(len(logs_in)):
            return logs_in[i].user
        """    
            
            
            
            
            