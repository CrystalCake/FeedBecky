#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

from DAO import *
from gpiozero import LED
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
raum = '9-108'
led = LED(21)

try:
    while(True):
        vorlesungsID = get_open_vorlesungs_id(raum)
        print("VorlesungsID = " + str(vorlesungsID))
        if vorlesungsID == 0:
            print('no running course')
        else:
            print('no Card')
            id, rating = reader.read()
            led.on()
            time.sleep(0.5)
            led.off();
            try:
                rating = int(rating);
            except ValueError:
                continue;
            print("transponder id ="+str(id))
            print("rating = "+str(rating))
            post_bewertung(int(rating), vorlesungsID)
        time.sleep(0.75)
#Übergabe an Interface

except KeyboardInterrupt:
	GPIO.cleanup()