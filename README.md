# IoTFeedbackSystem

## Installation

### Hardware
Für Das Projekt wird folgende Hardware benötigt: (verlinkt sind die für den PoC genutzen Komponeten)
  -  [1x Raspberry Pi 4](https://www.amazon.de/dp/B07W7Q6ZC9/?coliid=IZF6YUG2OX3TS&colid=2X693NO2NPXBG&psc=1&ref_=lv_ov_lig_dp_it)
  -  [1x Raspberry Pi Zero](https://www.amazon.de/dp/B072LWBL37/?coliid=I1YLWHU8D9MAOJ&colid=2X693NO2NPXBG&psc=0&ref_=lv_ov_lig_dp_it)
  - [2x RFID - Reader](https://www.amazon.de/dp/B076HSDF2Y/?coliid=I2YK48HJ96HRZJ&colid=2X693NO2NPXBG&psc=1&ref_=lv_ov_lig_dp_it)
  - [1x RFID - Karte](https://www.amazon.de/dp/B076HSDF2Y/?coliid=I2YK48HJ96HRZJ&colid=2X693NO2NPXBG&psc=1&ref_=lv_ov_lig_dp_it)
  - [5x RFID - Chips](https://www.amazon.de/dp/B076HSDF2Y/?coliid=I2YK48HJ96HRZJ&colid=2X693NO2NPXBG&psc=1&ref_=lv_ov_lig_dp_it)
  - [1x 5'' Bildschrim für Raspberry Pi](https://www.amazon.de/dp/B07YCBWRQP/?coliid=I2CIO40FHBZFQE&colid=2X693NO2NPXBG&psc=1&ref_=lv_ov_lig_dp_it)
  
Getestet wurde FeedBecky bisher nur auf dem Pi4 4GB. Das Rating Modul wurde zusätzlich noch mit einem Pi Zero getestet.


### Libraries & Frameworks
Um die Python-Skripte zu starten werden einige Libraries benötigt.
  - [Python3](https://www.python.org/) - Zum ausführen der Skripte.
  - [PyQt5](https://pypi.org/project/PyQt5/)  - Als UI Framework.
  - [QtChart](https://doc.qt.io/qt-5/qtcharts-index.html) - Für die Darstellung der Auswertungsgraphen.
  - [mfrc522](https://github.com/miguelbalboa/rfid) - Librarie für den RFID-Reader.
  - [MariaDB](https://mariadb.com/) - Zum speichern der Vorlesungen, der Bewertungen und der Professoren.



### Einrichtung der MySQL - Datenbank
Nachdem sie die MariaDB installiert haben muss der SQL-Dumb importiert werden. Dann müssen Sie die DAO.py auf ihren DB Nutzer anpassen oder den Nutzer "gast" mit dem Passwort "SECRET" anlegen. 

### Einrichtung der Raspberry Pies
Als erstes müssen Sie sich entscheiden ob welcher der Pies als "Professoren PI" und welcher als "Bewertungs PI" genutzt wird. Dementsprechend werden unterschiedliche Skripte gestartet. Auf dem "Professoren PI" starten Sie UI.py

```bash
python3 UI.py
```

Danach starten Sie das rating.py Skript auf dem "Bewertungs PI"
```bash
python3 rating.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
