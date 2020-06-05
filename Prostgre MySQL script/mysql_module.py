import mysql.connector

def connection ():

 #MySQL connection
 
 mydb = mysql.connector.connect(
  host="192.168.1.153",
  user="admin",
  passwd="P@ssw0rd",
  database="00_cos_warehouse"
  )
 print(mydb)

def test ():
    print("Hello world")