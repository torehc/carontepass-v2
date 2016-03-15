#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import time
import telebot

import urllib3
urllib3.disable_warnings()

from carontepass.settings_local import TOKEN_BOT, ID_GROUP_RECEIVER, ID_GROUP_LOG_RECEIVER

tb = telebot.TeleBot(TOKEN_BOT)


#Telegram message to users
def send_simple_msg(chatid, message):
  
    tb.send_message(chatid, message)


#Message to telegram group when entering the first or the last to leave out  
def send_group_msg(SiteOpen, user_name):
  
    if SiteOpen == True:
      tb.send_message(ID_GROUP_RECEIVER, "Site Open ("+user_name+")" )
    else:
      tb.send_message(ID_GROUP_RECEIVER, "Site Closed ("+user_name+")") 
      

#Message to telegram group only with entry and exit logs      
def send_log_msg(User_In, user_name):

    if User_In == True:
      tb.send_message(ID_GROUP_LOG_RECEIVER, "Come In: "+user_name )
    else:
      tb.send_message(ID_GROUP_LOG_RECEIVER, "Come Out: "+user_name )