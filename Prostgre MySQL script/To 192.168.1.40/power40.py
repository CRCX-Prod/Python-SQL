import psycopg2
import mysql.connector
import postgre_to_mysql
from datetime import datetime

now = datetime.now()

start_time = now.strftime("20%y-%m-%d %H:%M:%S")
print("Start at ", start_time)


#__________________
#Postgre Connection

postConn = psycopg2.connect(
    host="192.168.1.16",
    port = 5432,
    database="report_db_apollo_towers",
    user="datawarehouse",
    password="HPdhyHCYc8SfLY05EZKOSeH1ekoMXgzZuf44d4gP"
    )

#________________
#MySQL Connection

mysqlConn = mysql.connector.connect(
    host="192.168.1.40",
    user="script.update",
    passwd="zy6BjHr4k@sFa",
    database="cos_python"
    )

#___________
#Update O&M actions

table = "service_work_order"

postQuery = """select
  b_swo.data->'swo_id' as "SWO ID",
  b_swo.data->>'anchor_id' as "Anchor ID",
  b_swo.data->>'site_id_text' as "Site ID",
  b_swo.data->>'zone_team' as "Zone",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 128 AND field_id = '2' AND option_id = b_swo.data->>'swo_type'), '') as "SWO Type", 
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 93 AND value_id = b_swo.data->>'swo_category'), '') as "SWO Category",
  b_swo.data->>'swo_description' as "SWO Description",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_swo.data->>'swo_creation_date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "SWO Creation Date",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 90 AND field_id = '145' AND option_id = b_swo.data->>'region'), '') as "Region",  
  b_swo.data->>'team' as "Team",
  b_swo.data->>'o_m_vendor' as "O&M Vendor",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 128 AND field_id = '6' AND option_id = b_swo.data->>'priority'), '') as "Priority",  
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 128 AND field_id = '6' AND option_id = b_swo.data->>'planned_closed_date'), '') as "Planned close date", 
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_swo.data->>'swo_close_date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "SWO Close date",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 128 AND field_id = '7' AND option_id = b_swo.data->>'swo_status'), '') as "SWO Status",
  b_swo.data->>'remark' as "Remark",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_swo.data->>'last_change','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Last change",
  b_swo.data->>'created_by' as "Created by"
 FROM forms_data as b_swo
 WHERE b_swo.form_id in (128) AND 
  b_swo.enabled  = true AND 
 ( b_swo.embedded = false OR b_swo.embedded is null)
 """

#postgre_to_mysql.rebuildFromQuery(postConn,mysqlConn,table,postQuery)
#postgre_to_mysql.createFromQuery(postConn,mysqlConn,table,postQuery)
postgre_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)


#__________
#Record log

now = datetime.now()

end_time = now.strftime("20%y-%m-%d %H:%M:%S")
print("End at ", end_time)

mycursor = mysqlConn.cursor()

sql = "INSERT INTO 00_log_script (script_name, start, end) VALUES (%s, %s, %s)"
val = ("power.py", start_time, end_time)
mycursor.execute(sql, val)

mysqlConn.commit()