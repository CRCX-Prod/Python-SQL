import psycopg2
import mysql.connector
import postgre_to_mysql
import postgre_module
import cx_Oracle
from datetime import datetime



"""
postConn = cx_Oracle.connect(
    host="1192.168.1.62", 
    port = 1521, 
    database="itower2", 
    user="charles", 
    password="crich2020"
    )
"""

user='charles'
password = 'crich2020'
dsn= "192.168.1.62:1521/itower2"

conn = cx_Oracle.connect("charles", "crich2020", "192.168.1.62:1521/itower2") 