import mysql.connector

#________________
#MySQL connection


def connection():
 
    mydb = mysql.connector.connect(
    host="192.168.1.153",
    user="admin",
    passwd="P@ssw0rd",
    database="00_python"
    )

#__________________________________
#format From Prosgre query to MySQL

def formatColumns(postgreColumns):

    #Change in string
    myColumns = str(postgreColumns)
    #format Columns
    myColumns = myColumns.replace("[","(")
    myColumns = myColumns.replace("]",")")
    myColumns = myColumns.replace("'","`")

    return myColumns

#______________________________
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

#____________________
#Insert data in table

def insertData (connection,myTable,myColumns,myData):

    """
    mydb = mysql.connector.connect(
        host="192.168.1.153",
        user="admin",
        passwd="P@ssw0rd",
        database="00_cos_warehouse"
        )
    """    
    mycursor = connection.cursor()

    myColumnsString = formatColumns(myColumns)
    myIncr = formatIncr(myColumns)

    sql = "INSERT INTO {} {} VALUES {}"
    sql = sql.format(myTable,myColumnsString,myIncr)

    mycursor.execute(sql, myData)
    connection.commit()

    print(mycursor.rowcount, "records inserted in ",myTable)

def dropTable (connection,myTable):
    
    """
    mydb = mysql.connector.connect(
        host="192.168.1.153",
        user="admin",
        passwd="P@ssw0rd",
        database="00_cos_warehouse"
        )
    """

    mycursor = connection.cursor()

    sql = "DROP TABLE {}"
    sql = sql.format(myTable)

    mycursor.execute(sql) 
    
    print("Table "+ myTable +" dropped")
    

def createTable (connection,myTable,myColumns):

    """
    mydb = mysql.connector.connect(
        host="192.168.1.153",
        user="admin",
        passwd="P@ssw0rd",
        database="00_cos_warehouse"
        )
    """

    mycursor = connection.cursor()
    
    sItem = "`{}` VARCHAR(255)"
    lColumns = []
    for x in myColumns:
       lColumns.append(sItem.format(x))
   
    sColumns = str(lColumns)
    sColumns = sColumns.replace("[","(")
    sColumns = sColumns.replace("]",")")
    sColumns = sColumns.replace("'","")

    #sql = "CREATE TABLE customers (`col1` VARCHAR(255), 'col2' VARCHAR(255))")
    sql = "CREATE TABLE {} {}"
    sql = sql.format(myTable,sColumns)

    mycursor.execute(sql)
    connection.commit()
    print("Table "+ myTable + " created")

