#Airtable library
import os
from pprint import pprint
from airtable import Airtable
import airtable_module
#MySQL library
import mysql_module
import mysql.connector

#________________
#MySQL Connection

mysqlConn = mysql.connector.connect(
    host="192.168.1.40",
    user="script.update",
    passwd="zy6BjHr4k@sFa",
    database="test_python"
    )

base = 'appIZ8SjK4PI6fDWc'
table = 'Sites'
view = 'Python test'

query = airtable_module.queryAirtable(base,table,view)
airColumns = airtable_module.getColumns (query)
airData = airtable_module.getData(query)


def getData (query):

    column_step1 = list(query[0].values())
    column_step2 = column_step1[1]
    columns_result = list(column_step2)

    print(query)
    print (columns_result)
    #Process list
    for x in range(len(query)):

        data_step1 = list(query[x].values())
        data_step2 = data_step1[1]
        dataItem = tuple(data_step2.values())

        #print(dataItem)
        if x==0:
            dataList =(dataItem,)  #For first item
            continue
        dataList = dataList+(dataItem,)
        #dataList = dataList+(dataItem,)

    #dataList = dataList,dataItem
    return dataList


test = getData (query)




#print (airData)

#def insertData (connection,myTable,myColumns,myData):
#mysql_module.createTable (mysqlConn,view,airColumns)
#mysql_module.insertData (mysqlConn,view,airColumns,airData)