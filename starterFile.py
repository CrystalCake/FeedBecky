import RPi.GPIO as GPIO
import time
import DAO
import UI

from mfrc522 import SimpleMFRC522

#waiting for Card
while True:
    try:
        #showing LoginScreen
        UI.showLoginScreen()

        #if card found read
        id, prof_id = reader.read()
        print(id)
        print(text)

        #getEssentials & start Lecture
        if(prof_id != None)
            prof_name = DAO.get_prof_name(prof_id)
            DAO.create_vorlesung(prof_id, "TestVorlesung")
            UI.showVorlesungsScreen(prof_name)

        time.sleep(2)

        #Übergabe an Interface

    except KeyboardInterrupt:
        GPIO.cleanup()