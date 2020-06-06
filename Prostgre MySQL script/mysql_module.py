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

#format From Prosgre query to MySQL
def formatColumns(postgreColumns):

    #Change in string
    myColumns = str(postgreColumns)
    #format Columns
    myColumns = myColumns.replace("[","(")
    myColumns = myColumns.replace("]",")")
    myColumns = myColumns.replace("'","`")

    return myColumns

#Create the (%s, %s,...) string
def formatIncr (postgreColumns):

    myIncr = []
    for x in postgreColumns:
       myIncr.append("%s")

    myIncr = str(myIncr)
    myIncr = myIncr.replace("[","(")
    myIncr = myIncr.replace("]",")")
    myIncr = myIncr.replace("'","")

    return myIncr


#Insert data
def insertData (myTable,myColumns,myData):

    """
    mydb = mysql.connector.connect(
        host="192.168.1.153",
        user="admin",
        passwd="P@ssw0rd",
        database="00_cos_warehouse"
        )
    """
    
    table = myTable
    
    myColumnsString = formatColumns(myColumns)
    myIncr = formatIncr(myColumns)

    sql = "INSERT INTO {} {} VALUES {}"
    sql = sql.format(myTable,myColumnsString,myIncr)

mycursor = mydb.cursor()

sql = "INSERT INTO site_script (Site ID, Entity) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

