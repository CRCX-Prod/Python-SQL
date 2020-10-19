import cx_Oracle
import mysql.connector
import oracle_to_mysql
from datetime import datetime

now = datetime.now()

start_time = now.strftime("20%y-%m-%d %H:%M:%S")
print("Start at ", start_time)

#__________________
#Oracle Connection


postConn = cx_Oracle.connect("charles","crich2020","192.168.1.62/ITOWER2")

#________________
#MySQL Connection

mysqlConn = mysql.connector.connect(
    host="192.168.1.153",
    user="admin",
    passwd="P@ssw0rd",
    database="00_python"
    )

#___________
#Create in MySQL itower_test table

table = "itower_test"

postQuery = """SELECT * FROM ITOWERDATA.TXN_SITE_DOWN_TICKETS WHERE ROWNUM < 3"""

#poracle_to_mysql.rebuildFromQuery(postConn,mysqlConn,table,postQuery)
#oracle_to_mysql.createFromQuery(postConn,mysqlConn,table,postQuery)
oracle_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)