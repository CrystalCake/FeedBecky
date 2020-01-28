from datetime import datetime

class DAO():

    def __init__(self):
        #super().__init__()

        #Variablen initialisieren
        self.IP_ADDRESS = "localhost"
        self.LOGIN = "admin"
        self.PASSWORD = "1234"
        self.PROF_TABLE = "users"
        self.VORLESUNG_TABLE = "Vorlesung"
        self.BEWERTUNGEN_TABLE = "Bewertung"
        self.raum = "9-108"

        self.PROF_db = pymysql.connect(IP_ADDRESS, LOGIN, PASSWORD, PROF_TABLE)
        self.PROF_cursor = PROF_db.cursor()

        self.VORLESUNG_db = pymysql.connect(IP_ADDRESS, LOGIN, PASSWORD, VORLESUNG_TABLE)
        self.VORLESUNG_cursor = VORLESUNG_db.cursor()

        self.BEWERTUNG_db = pymysql.connect(IP_ADDRESS, LOGIN, PASSWORD, BEWERTUNGEN_TABLE)
        self.BEWERTUNG_cursor = BEWERTUNG_db.cursor()


    def read_prof(self, prof_id):
        self.PROF_cursor.execute("SELECT * FROM user where name=%s", prof_name)
        records = self.PROF_cursor.fetchall()
        for row in records:
            return row[0]
        return 0;


    def create_vorlesung(self, prof_id, lec_name):
        self.VORLESUNG_cursor.execute("INSERT INTO vorlesung (name, profID, raum) VALUES (name=%s, profID=%s, raum=%s)", [lec_name, prof_id, raum])
        return 0;

    def update_vorlesung(self, vorlesungs_ID):
        self.VORLESUNG_cursor.execute("UPDATE vorlesung SET (endDatum = datetime.now()) WHERE id=%s", [vorlesungs_ID])
        return 0;

    def get_prof_name(self, prof_ID):
        self.PROF_cursor.execute("SELECT * FROM user where id=%s", prof_ID)
        records = PROF_cursor.fetchall()
        for row in records:
            return row[1]
        return 0;

    def get_vorlesungen(self, prof_ID):
        self.PROF_cursor.execute("SELECT * FROM Vorlesung WHERE id=%s", [prof_ID])
        return PROF_cursor.fetchall()
        return 0;

    def get_bewertungen(self, vorlesungs_ID):
        self.PROF_cursor.execute("SELECT * FROM Bewertung WHERE id=%s", [vorlesungs_ID])
        return self.PROF_cursor.fetchall()
        return 0;

    def post_bewertung(self, wert, vorlesungs_ID):
        self.VORLESUNG_cursor.execute("INSERT INTO bewertung (wert) VALUES (wert=%s) WHERE id=%s", [wert, vorlesungs_ID])
        return 0;
