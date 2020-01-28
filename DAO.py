from datetime import datetime
import pymysql

import pymysql


class DAO():

    def __init__(self):
        #Variablen initialisieren

        self.IP_ADDRESS = "192.168.137.140"
        self.LOGIN = "gast"
        self.PASSWORD = "SECRET"
        self.DB = "users"
        self.raum = "9-108"


        self.db = pymysql.connect(self.IP_ADDRESS, self.LOGIN, self.PASSWORD, self.DB)
        self.cursor = self.db.cursor()


    def read_prof(self, prof_id):
        self.cursor.execute("SELECT * FROM user where id=%s", [prof_id])
        records = self.cursor.fetchall()
        for row in records:
            return row[0]
        return 0;


    def create_vorlesung(self, prof_id, lec_name):
        self.cursor.execute("INSERT INTO vorlesung (name, profID, raum) VALUES (name=%s, profID=%s, raum=%s)", [lec_name, prof_id, raum])
        return 0;

    def update_vorlesung(self, vorlesungs_ID):
        self.cursor.execute("UPDATE vorlesung SET (endDatum = datetime.now()) WHERE id=%s", [vorlesungs_ID])
        return 0;

    def get_prof_name(self, prof_ID):
        self.cursor.execute("SELECT * FROM user where id=%s", prof_ID)
        records = self.cursor.fetchall()
        for row in records:
            return row[1]
        return 0;

    def get_vorlesungen(self, prof_ID):
        self.cursor.execute("SELECT * FROM Vorlesung WHERE id=%s", [prof_ID])
        return self.cursor.fetchall()
        return 0;

    def get_bewertungen(self, vorlesungs_ID):
        self.cursor.execute("SELECT * FROM Bewertung WHERE id=%s", [vorlesungs_ID])
        return self.cursor.fetchall()
        return 0;

    def post_bewertung(self, wert, vorlesungs_ID):
        self.cursor.execute("INSERT INTO bewertung (wert) VALUES (wert=%s) WHERE id=%s", [wert, vorlesungs_ID])
        return 0;
