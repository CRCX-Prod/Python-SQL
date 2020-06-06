import psycopg2
import mysql_module
import postgre_module

postgreQuery = """Select b_sites.data->>'site_id_text' as "Site ID" ,  
 COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 32 AND value_id = b_sites.data->>'entity'), '') as "Entity"
 FROM forms_data as b_sites 
 WHERE b_sites.form_id in (97) AND 
  b_sites.enabled  = true AND 
 ( b_sites.embedded = false OR b_sites.embedded is null) AND 
 ((b_sites.data ->>'site_id_text') IN ('1-01-17006-005'))
 """

postgreConn = psycopg2.connect(
    host="192.168.1.16", 
    port = 5432, 
    database="report_db_apollo_towers", 
    user="datawarehouse", 
    password="HPdhyHCYc8SfLY05EZKOSeH1ekoMXgzZuf44d4gP"
    )

#mysql_module.connection ()

#Working
queryColumns = postgre_module.getColumns (postgreConn,postgreQuery)

queryData = postgre_module.getData (postgreConn,postgreQuery)

print(queryColumns)

print(queryData)

postgreConn.close()

mysql_module.insertData("Table",queryColumns,queryData)

