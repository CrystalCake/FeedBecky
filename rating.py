#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import pymysql

from DAO import *
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
vorlesungsID = 26
try:
    print('no Card')
    id, rating = reader.read()
    print(id)
    print(rating)
    post_bewertung(rating, vorlesungsID)
    time.sleep(1.5)
#Übergabe an Interface

except KeyboardInterrupt:
	GPIO.cleanup()