#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import os
import requests
import json
import RPi.GPIO as GPIO
from time import sleep
import RPi.GPIO as GPIO
import MFRC522
import signal


def get_json(tag=''):

    domain = "192.168.1.XX:8000" #IP-Server

    url = "http://"+domain+"/api/1/device/"+tag

    r = requests.get(url, auth=('user', 'pass')) #User Admin/Staff

    print(url)
    print(r.json())
    print("----------------")
    
    
    parsed_json = r.json()
    result = parsed_json[0]['result']
    
    return result


def action(result):
    '''
    '''
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(24, GPIO.OUT)
    
    if result:
        print "Relay ON"
        GPIO.output(24, GPIO.LOW)
        sleep(1.5)
        GPIO.output(24, GPIO.HIGH)
    else:
        print "Relay OFF"



if __name__ == '__main__':
    
    continue_reading = True

    # Capture SIGINT for cleanup when the script is aborted
    def end_read(signal,frame):
        global continue_reading
        print "Ctrl+C captured, ending read."
        continue_reading = False
        GPIO.cleanup()
    
    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)
    
    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()
    
    # Welcome message
    print "Welcome to CarontePass"
    print "Press Ctrl-C to stop."
    
    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    while continue_reading:

        # Scan for cards      
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    
        # If a card is found  
        if status == MIFAREReader.MI_OK:
            print "Card detected"
    
        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
    
        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            # Print UID
	    print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])

            # Make tag
            tag = '.'.join([str(x) for x in uid[:-1]])

            result = get_json(tag)

            # Activate relay
            action(result)
