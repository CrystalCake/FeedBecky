#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys

from DAO import *
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

vorlesungsID = sys.argv[1]

try:
    while(True):
        print('no Card')
        id, rating = reader.read()
        print("transponder id ="+id)
        print("rating = "+rating)
        post_bewertung(int(rating), vorlesungsID)
        time.sleep(1.5)
#Übergabe an Interface

except KeyboardInterrupt:
	GPIO.cleanup()