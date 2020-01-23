import pymysql

IP_ADDRESS = "localhost"
LOGIN = "admin"
PASSWORD = "1234"
PROF_TABLE = "users"
VORLESUNG_TABLE = "Vorlesung"
BEWERTUNGEN_TABLE = "Bewertung"

PROF_db = pymysql.connect(IP_ADDRESS, LOGIN, PASSWORD, PROF_TABLE)
PROF_cursor = PROF_db.cursor()

VORLESUNG_db = pymysql.connect(IP_ADDRESS, LOGIN, PASSWORD, PROF_TABLE)
VORLESUNG_cursor = VORLESUNG_db.cursor()


def read_prof(prof_name):
    PROF_cursor.execute("SELECT * FROM user where name=%s", prof_name)
    records = PROF_cursor.fetchall()
    for row in records:
        return row[0]
    return 0;

def create_vorlesung():

    return 0;

def update_vorlesung(vorlesungs_ID):

    return 0;

def get_prof_name(prof_ID):
    PROF_cursor.execute("SELECT * FROM user where ID=%s", prof_ID)
    records = PROF_cursor.fetchall()
    for row in records:
        return row[1]
    return 0;

def get_vorlesungen(prof_ID):
    PROF_cursor.execute("SELECT * FROM Vorlesung WHERE profID=%s", [prof_ID])
    return PROF_cursor.fetchall()

    return 0;

def get_bewertungen(vorlesungs_ID):
    PROF_cursor.execute("SELECT * FROM Bewertung WHERE vorlesungs_ID=%s", [vorlesungs_ID])
    return PROF_cursor.fetchall()

    return 0;

def post_bewertung(bewertung, vorlesungs_ID):

    return 0;
