import postgre_module
import postgre_to_mysql


#create a MySQL table from a PostgreQuery 
def insertFromQuery (postConn,myConn,tableName,postQuery):
    
    postColumns = postgre_module.getColumns(postConn,postQuery)
    postData = postgre_module.getData(postConn,postQuery)

    mysql_module.dropTable(myConn,tableName)
    mysql_module.createTable(myConn,tableName,postColumns)
    mysql_module.insertData(myConn,tableName,postColumns,postData)