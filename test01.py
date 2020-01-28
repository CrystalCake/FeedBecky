#!/usr/bin/env python

import RPi.GPIO as GPIO
import threading
import time
import UI


from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


class UiHandling(threading.Thread):
    
    def run(self):
        UI.main()


t = UiHandling()
t.start()

class Logik():
    
    try:
        print('no Card')
        id, text = reader.read()
        print(id)
        print(text)
        #bewertung = (1,2,5,2,4)

        UI.Screens.showVorlesungsScreen(UI.Screens, "Decker")

        time.sleep(0.1)

        #Übergabe an Interface

    except KeyboardInterrupt:
        GPIO.cleanup()


        #screens.showBewertungsScreen(bewertung, 5)

