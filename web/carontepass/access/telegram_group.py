#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import time
import telebot

import urllib3
urllib3.disable_warnings()

#Token of your bot
TOKEN = 'xxxxxx'

#Receptor chat id
IDchatReceiver = 'xxxxxxx'

tb = telebot.TeleBot(TOKEN)

def send_group_msg(message):
  
  tb.send_message(IDchatReceive, message)
