

IP_ADDRESS = "localhost"
LOGIN = "admin"
PASSWORD = "1234"
PROF_TABLE = "users"
VORLESUNG_TABLE = ""



db = pymysql.connect("localhost", "admin", "1234", "users")
curs= db.cursor()


def read_prof():

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