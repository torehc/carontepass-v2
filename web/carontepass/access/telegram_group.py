#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import time
import telebot

import urllib3
urllib3.disable_warnings()

from carontepass.settings import TOKEN_BOT, ID_CHAT_RECEIVER

#id of the person receiving the telegram messages
IDchatReceiver = ID_CHAT_RECEIVER

tb = telebot.TeleBot(TOKEN_BOT)


def send_simple_msg(chatid, message):
  
    tb.send_message(chatid, message)

  
def send_group_msg(SiteOpen, user_name):
  
    if SiteOpen == True:
      tb.send_message(IDchatReceiver, "Site Open ("+user_name+")" )
    else:
      tb.send_message(IDchatReceiver, "Site Closed ("+user_name+")" )