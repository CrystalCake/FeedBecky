import sys
from PyQt5 import QtWidgets, QtCore, QtChart
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
        self.LoginWindow.setStyleSheet("background-image: url(welcome.png);")

        #Ansicht zusammenstellen
        self.LoginWindow.setLayout(layout)
        self.LoginWindow.show()


    def showVorlesungsScreen(self, name):
        # Andere Fenster schließen
        self.LoginWindow.hide()
        self.BewertungsWindow.hide()

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

    def showBewertungsScreen(self, bewertungen, maxWert):
        # Andere Fenster schließen
        self.LoginWindow.hide()
        self.VorlesungWindow.hide()

        # Vorlesungsfenster erstellen
        self.BewertungsWindow.setMinimumHeight(480)
        self.BewertungsWindow.setMinimumWidth(800)
        
        #Layout festlegen
        layout = QtWidgets.QGridLayout()
        
        #Sets erstellen (unterteilt nach Noten)
        self.set = QtChart.QBarSet ('Gut')
        self.set1 = QtChart.QBarSet ('Okay')
        self.set2 = QtChart.QBarSet ('Zu Langsam')
        self.set3 = QtChart.QBarSet ('Zu Schnell')
        self.set4 = QtChart.QBarSet ('Zu Kompliziert')
        
        self.set.append(bewertungen[0])
        self.set1.append(bewertungen[1])
        self.set2.append(bewertungen[2])
        self.set3.append(bewertungen[3])
        self.set4.append(bewertungen[4])
        
        #Einzelne Graphen erstellen und mit Sets verknüpfen
        self.series = QtChart.QBarSeries()
        self.series.append(self.set)
        self.series.append(self.set1)
        self.series.append(self.set2)
        self.series.append(self.set3)
        self.series.append(self.set4)
        
        #Chart initialiseren und Start Animation festlegen
        self.chart = QtChart.QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Bewertungen")
        self.chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        
        #Achsen erstellen und formatieren
        achseX = QtChart.QBarCategoryAxis()
        achseY = QtChart.QValueAxis()
        achseY.setRange(0,maxWert)
        
        #Ansicht zusammenstellen und anzeigen
        self.chart.addAxis(achseX, QtCore.Qt.AlignBottom)
        self.chart.addAxis(achseY, QtCore.Qt.AlignLeft)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(QtCore.Qt.AlignBottom)
        chartView = QtChart.QChartView(self.chart)
        layout.addWidget(chartView)
        self.BewertungsWindow.setLayout(layout)
        self.BewertungsWindow.show()
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    screens = Screens()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

