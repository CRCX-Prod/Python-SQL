#Airtable library
import os
from pprint import pprint
from airtable import Airtable
#MySQL library
import mysql_module
import mysql.connector

#____________________________________________________________

"""
airtable = Airtable('appCeehu9RgHJAPYY','Table 1',api_key='key2oMENkcz6kdrIy')

print(airtable.get_all(view='Name',sort='Notes'))
print(airtable.get_all())
"""

##airtable.create('Table 1', {"Name":"Test import Python"})


#____________________________________________________________
#File name airtable_test.py
#Fonctionne 
"""
airtable = Airtable('appIZ8SjK4PI6fDWc','Sites',api_key='key2oMENkcz6kdrIy')

airtable.update_by_field('AP SITE ID', 'AYYN_0138', {'Site survey': 'Test script'})
"""

#________________
#MySQL Connection


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
Test = mysql_module.getColumns (mysqlConn,queryMySQL)
print(Test)

Test2 = mysql_module.getData (mysqlConn,queryMySQL)
print(Test2)

#Functions Airtable
"""
def updateAirtableLine ()

def createAirtableLine ()

def AirtableConnection ()
"""