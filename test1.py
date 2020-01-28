#!/usr/bin/env python

#import RPi.GPIO as GPIO
import time
from UI import Screens

#from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
UI.main()
screens = Screens()

screens.showLoginScreen()

try:
	print('no Card')
	#id, text = reader.read()
	print(id)
	print(text)
	#bewertung = (1,2,5,2,4)
	screens.showVorlesungsScreen("Decker")


	time.sleep(0.1)

	#Übergabe an Interface

except KeyboardInterrupt:
	#GPIO.cleanup()


	#screens.showBewertungsScreen(bewertung, 5)

