

IP_ADDRESS = "localhost"
LOGIN = "admin"
PASSWORD = "1234"
PROF_TABLE = "users"
VORLESUNG_TABLE = ""

PROF_db = pymysql.connect(IP_ADDRESS, LOGIN, PASSWORD, PROF_TABLE)
PROF_cursor = PROF_db.cursor()

VORLESUNG_db = pymysql.connect(IP_ADDRESS, LOGIN, PASSWORD, PROF_TABLE)
VORLESUNG_cursor = VORLESUNG_db.cursor()


def read_prof():
    PROF_cursor.execute("SELECT * FROM user where name=%s", [text])
    records = PROF_cursor.fetchall()
    for row in records:
        PROF_cursor.execute("SELECT * FROM Vorlesung WHERE profID=%s", [row[0]])
        vorlesungRec = PROF_cursor.fetchall()
    return 0;

def create_vorlesung():

    return 0;

def update_vorlesung(vorlesungs_ID):

    return 0;

def get_prof_name(prof_ID):

    return 0;

def get_vorlesungen(prof_ID):

    return 0;

def get_bewertungen(vorlesungs_ID):

    return 0;

def post_bewertung(bewertung, vorlesungs_ID):

    return 0;