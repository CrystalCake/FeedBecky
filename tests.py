#tests

#from DAO import DAO

print("Hello World!")
#dao = DAO();
#prof = dao.read_prof(1)
#print(prof)

import pymysql
import pymysql.cursors

# Connect to the database
connection = pymysql.connect("192.168.137.140", "admin", "1234", "users")
