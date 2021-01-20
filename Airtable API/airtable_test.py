#Airtable library
import os
from pprint import pprint
from airtable import Airtable
#MySQL library
import mysql_module
import mysql.connector

#Functions Airtable
"""
def AirtableConnection ()
  
  airtable = Airtable('appIZ8SjK4PI6fDWc','Sites',api_key='key2oMENkcz6kdrIy')

def createAirtableLine ()

def AirtableConnection ()
"""

#Old script
    import os
    from pprint import pprint
    from airtable import Airtable
    #MySQL library
    import mysql_module
    import mysql.connector

    mysqlConn = mysql.connector.connect(
        host="192.168.1.40",
        user="script.update",
        passwd="zy6BjHr4k@sFa",
        database="cos_python"
        )

    queryMySQL = """
      SELECT
        sites.`Site ID`,
        sites.Zone
      FROM sites
    """

    testList = mysql_module.getData (mysqlConn,queryMySQL)
    print (testList)
    def formatString(testList)
      
      stringFormat = testList
      
      return stringFormat

    testOutput = formatString (testList)
    print stringFormat


    baseID = 'appIZ8SjK4PI6fDWc'
    tableName = 'Sites'

    lookupColumn = 'AP Site ID'
    lookupData = 'AYYN_0138'

    updateColumns = 'Site survey'
    updateData = 'Test function script1'

    updateAirtableLine (baseID,tableName,lookupColumn,lookupData,updateColumns,updateData)

    #_____________________
    #END

  """
  def updateAirtableLine (baseID,tableName,lookupColumn,lookupData,updateColumns,updateData)

    #airtable = Airtable(baseID,tableName,api_key='key2oMENkcz6kdrIy')
    
    #airtable.update_by_field('AP SITE ID', 'AYYN_0138', {'Site survey': 'Test script'})
    #airtable.update_by_field(lookupColumn, lookupData, {'Site survey': 'Test script'})
    print (baseID,tableName,lookupColumn,lookupData,updateColumns,updateData)
  """




#___________________________
#Script V1

#Functions Airtable

#Airtable library
import os
from pprint import pprint
from airtable import Airtable
#MySQL library
import mysql_module
import mysql.connector

mysqlConn = mysql.connector.connect(
    host="192.168.1.40",
    user="script.update",
    passwd="zy6BjHr4k@sFa",
    database="cos_python"
    )

mysqlConn2 = mysql.connector.connect(
    host="192.168.1.40",
    user="script.update",
    passwd="zy6BjHr4k@sFa",
    database="cos_python"
    )

#Query to python lists
queryMySQL = """
SELECT
  sites.`Site ID`,
  sites.`Site status`,
  sites.`Site category`
FROM sites
WHERE sites.`Site ID` = 'ASMO_0176'
"""

ColumnSQL = mysql_module.getColumns (mysqlConn,queryMySQL)
DataSQL = mysql_module.getData (mysqlConn2,queryMySQL)


lookupColumn = ColumnSQL[0]
print (lookupColumn)

DataLine = DataSQL[0]
lookupData = DataLine [0]
print (lookupData)


stringUpdate = "{"

for i in range(len(ColumnSQL)):

   if i == 0: continue

   incrColumnSQL = ColumnSQL[i]
   incrLineSQL = DataLine[i]

   updateItem = "'{}': '{}'"
   updateItem = updateItem.format(incrColumnSQL,incrLineSQL)

   stringUpdate = stringUpdate + "'"
   stringUpdate = stringUpdate + incrColumnSQL + "' : '" + incrLineSQL +"'"

   if i == len(ColumnSQL) -1: break
   stringUpdate = stringUpdate + ','

stringUpdate = stringUpdate + "}"
#print (stringUpdate)

execAirtable = "airtable.update_by_field('" + lookupColumn
execAirtable = execAirtable + "','" + lookupData + "'," + stringUpdate + ")"
#print(execAirtable)

airtable = Airtable('appIZ8SjK4PI6fDWc','Sites',api_key='key2oMENkcz6kdrIy')

exec(execAirtable)

#airtable.update_by_field('SITE ID', 'AYYN_0138', {'Site survey': 'Test script','Label':'scriptons'})

#____________
#Select Airtable

#Airtable library
import os
from pprint import pprint
from airtable import Airtable
#MySQL library
import mysql_module
import mysql.connector

airtable = Airtable('appIZ8SjK4PI6fDWc','Sites',api_key='key2oMENkcz6kdrIy')

test = airtable.get_all(maxRecords=20)


test = airtable.get_all(maxRecords=20)


print(test)


step1 = list(test[0].values())
step2 = step1[1]
columnstep3 = list(step2)
datastep3 = list(step2.values())
print(columnstep3)
print(datastep3)


#airtable.get_all(view='MyView', maxRecords=20)