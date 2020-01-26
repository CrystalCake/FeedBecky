import sys
import time
from PyQt5 import QtWidgets, QtGui, QtCore
from datetime import datetime, timedelta

class Screens(QtWidgets.QWidget):


    def __init__(self):
        super().__init__()

        #Anwendungsfenster erstellen
        self.LoginWindow = QtWidgets.QWidget()
        self.VorlesungWindow = QtWidgets.QWidget()
        self.BewertungsWindow = QtWidgets.QWidget()

        #Variablen initialisieren
        self.zeitTracker = 0
        self.timerActive = True

        #Login Fenster starten
        self.showLoginScreen()


    #Seit Start vergangene Zeit tracken und updaten
    def updateTimeLabel(self):
        self.zeitTracker = self.zeitTracker + 1
        zeitString = str(timedelta(seconds=self.zeitTracker))
        self.zeitLabel.setText("Dauer der Vorlesung: " + zeitString)


    def showLoginScreen(self):
        #LoginFenster erstellen
        self.LoginWindow.setMinimumHeight(480)
        self.LoginWindow.setMinimumWidth(800)

        #Layout festlegen
        layout = QtWidgets.QGridLayout()

        #Willkommensbild einbinden
        welcomePic = QtWidgets.QLabel()
        welcomePixmap = QtGui.QPixmap("welcome.png")
        welcomePic.setPixmap(welcomePixmap)
        layout.addWidget(welcomePic)

        #Ansicht zusammenstellen
        self.LoginWindow.setLayout(layout)
        self.LoginWindow.show()
        self.showVorlesungsScreen("Decker(Testversion)")


    def showVorlesungsScreen(self, name):
        # Login Fenster schließen
        self.LoginWindow.hide()

        # Vorlesungsfenster erstellen
        self.VorlesungWindow.setMinimumHeight(480)
        self.VorlesungWindow.setMinimumWidth(800)
        self.VorlesungWindow.setStyleSheet("background-image: url(start.png);")

        # Layout festlegen
        layout = QtWidgets.QGridLayout()

        #Label erstellen
        self.nameLabel = QtWidgets.QLabel("Hallo Herr " + name)
        self.timeLabel = QtWidgets.QLabel("Start der Vorlesung: " + datetime.now().strftime("%H:%M"))
        self.zeitLabel = QtWidgets.QLabel("Vorlesung starten...")

        #Label designen (Alignment)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.zeitLabel.setAlignment(QtCore.Qt.AlignCenter)

        #Label designen (StyleSheets)
        self.nameLabel.setStyleSheet("font: 30pt; background: none")
        self.timeLabel.setStyleSheet("font: 20pt; background: none")
        self.zeitLabel.setStyleSheet("font: 20pt; background: none")

        # Ansicht zusammenstellen
        layout.addWidget(self.nameLabel, 0, 0, 1, 2)
        layout.addWidget(self.timeLabel)
        layout.addWidget(self.zeitLabel)
        self.VorlesungWindow.setLayout(layout)
        self.VorlesungWindow.show()

        #Timer für das update der Zeitanzeige starten
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateTimeLabel)
        self.timer.start(1000)


def main():
    app = QtWidgets.QApplication(sys.argv)
    screens = Screens()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

