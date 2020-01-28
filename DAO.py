import pymysql


#Variablen initialisieren

IP_ADDRESS = "192.168.137.140"
LOGIN = "gast"
PASSWORD = "SECRET"
DB = "users"
raum = "9-108"


db = pymysql.connect(IP_ADDRESS, LOGIN, PASSWORD, DB)
cursor = db.cursor()


def read_prof(prof_id):
    cursor.execute("SELECT * FROM user where id=%s", [prof_id])
    return cursor.fetchone()


##current_timestamp()
def create_vorlesung(prof_id, lec_name):
    cursor.execute("INSERT INTO Vorlesung (name, profID, raum) VALUES (%s, %s, %s)", [lec_name, prof_id, raum])
    db.commit()
    cursor.execute("SELECT id FROM Vorlesung "
                   "WHERE name = %s "
                   "AND profID = %s "
                   "AND raum = %s"
                   "AND startDatum = endDatum", [lec_name, prof_id, raum])
    return cursor.fetchall()[0][0]

def update_vorlesung(vorlesungs_ID):
    cursor.execute("UPDATE Vorlesung SET endDatum = current_timestamp() WHERE id=%s", [vorlesungs_ID])
    db.commit()
    return 0;

def get_prof_name(prof_ID):
    cursor.execute("SELECT * FROM user where id=%s", prof_ID)
    records = cursor.fetchall()
    for row in records:
        return row[1]
    return 0;

def get_vorlesungen(prof_ID):
    cursor.execute("SELECT * FROM Vorlesung WHERE id=%s", [prof_ID])
    return cursor.fetchall()
    return 0;

def get_bewertungen(vorlesungs_ID):
    cursor.execute("SELECT COUNT(*) FROM Bewertung WHERE vorlesungsID=%s AND wert=1", [vorlesungs_ID])
    records = cursor.fetchall()
    for row in records:
        wert_1 = row[0]
        
    cursor.execute("SELECT COUNT(*) FROM Bewertung WHERE vorlesungsID=%s AND wert=2", [vorlesungs_ID])
    records = cursor.fetchall()
    for row in records:
        wert_2 = row[0]
        
    cursor.execute("SELECT COUNT(*) FROM Bewertung WHERE vorlesungsID=%s AND wert=3", [vorlesungs_ID])
    records = cursor.fetchall()
    for row in records:
        wert_3 = row[0]
        
    cursor.execute("SELECT COUNT(*) FROM Bewertung WHERE vorlesungsID=%s AND wert=4", [vorlesungs_ID])
    records = cursor.fetchall()
    for row in records:
        wert_4 = row[0]
        
    
    cursor.execute("SELECT COUNT(*) FROM Bewertung WHERE vorlesungsID=%s AND wert=5", [vorlesungs_ID])
    records = cursor.fetchall()
    for row in records:
        wert_5 = row[0]
        
    return (wert_1, wert_2, wert_3, wert_4, wert_5)

def post_bewertung(wert, vorlesungs_ID):
    cursor.execute("INSERT INTO Bewertung (wert, vorlesungsID) VALUES (%s, %s)", [wert, vorlesungs_ID])
    db.commit()
    return 0;
