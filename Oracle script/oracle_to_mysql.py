import oracle_module
import mysql_module

#_________________________________________
#Append in MySQL table from a PostgreQuery
 
def insertFromQuery (postConn,myConn,tableName,postQuery):
    
    postColumns = oracle_module.getColumns(postConn,postQuery)
    postData = oracle_module.getData(postConn,postQuery)

    mysql_module.insertData(myConn,tableName,postColumns,postData)

#____________________________________________________________
#truncate and insert in a MySQL table from a PostgreQuery

def repopulateFromQuery (postConn,myConn,tableName,postQuery):
    
    postColumns = oracle_module.getColumns(postConn,postQuery)
    postData = oracle_module.getData(postConn,postQuery)

    mysql_module.truncateData(myConn,tableName,postColumns)
    mysql_module.insertData(myConn,tableName,postColumns,postData)


#____________________________________________________________
#drop, create and insert in a MySQL table from a PostgreQuery

def rebuildFromQuery (postConn,myConn,tableName,postQuery):
    
    postColumns = oracle_module.getColumns(postConn,postQuery)
    postData = oracle_module.getData(postConn,postQuery)

    mysql_module.dropTable(myConn,tableName)
    mysql_module.createTable(myConn,tableName,postColumns)
#    mysql_module.truncateData(myConn,tableName,postColumns)
    mysql_module.insertData(myConn,tableName,postColumns,postData)

#______________________________________________________
#create and insert in a MySQL table from a PostgreQuery

def createFromQuery (postConn,myConn,tableName,postQuery):
    
    postColumns = oracle_module.getColumns(postConn,postQuery)
    postData = oracle_module.getData(postConn,postQuery)

    mysql_module.createTable(myConn,tableName,postColumns)
    mysql_module.insertData(myConn,tableName,postColumns,postData)
    