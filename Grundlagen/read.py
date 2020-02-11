#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import pymysql

from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	print('no Card')
	id, text = reader.read()
	print(id)
	print(text)
	curs.execute("SELECT * FROM user where name=%s",[text])
	records = curs.fetchall()
	for row in records:
		curs.execute("SELECT * FROM Vorlesung WHERE profID=%s",[row[0]])
		vorlesungRec = curs.fetchall()
		print("Wilkommen " + row[1])
		for row2 in vorlesungRec:
			print("Vorlesung: " + row2[1])

	time.sleep(0.1)

	#Übergabe an Interface

except KeyboardInterrupt:
	GPIO.cleanup()

