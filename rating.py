#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import pymysql

from DAO import *
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print('no Card')
    id, rating = reader.read()
    print(id)
    print(rating)
    post_bewertung(rating, 26)

#Übergabe an Interface

except KeyboardInterrupt:
	GPIO.cleanup()