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
  b_swo.data->'action_id' ->>'prefix' as "Action ID - prefix",
  b_swo.data->'action_id' ->>'number' as "Action ID  - number",
  b_swo.data->'action_id' ->>'number' as "Action ID",
  b_swo.data->>'anchor_id' as "Anchor ID",
  b_swo.data->>'site_id_text' as "Site ID",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 32 AND value_id = b_swo.data->>'entity'), '') as "Entity",
  b_swo.data->>'zone_team' as "Zone",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 63 AND value_id = b_swo.data->>'anchor_class'), '') as "Anchor class",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 63 AND value_id = b_swo.data->>'power_configuration'), '') as "Power configuration",
  b_swo.data->>'week' as "Week",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_swo.data->>'date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Open date",
  b_swo.data->>'week_raw_sla' as "Week raw SLA",
  b_swo.data->>'repetitive_outages' as "Repetitive outages",
  b_swo.data->>'most_frequent_rca' as "RCA",
  b_swo.data->>'rca_sub_category' as "RCA sub category",
  b_swo.data->>'rca_summary' as "RCA summary",
  b_swo.data->>'battery_backup_duration' as "Battery backup duration",
  b_swo.data->>'grid_outage_duration' as "Grid outage duration",  
  b_swo.data->>'action_plan' as "Action plan",
  b_swo.data->>'action_by' as "Action by",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_swo.data->>'action_due','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Action due",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 120 AND field_id = '13' AND option_id = b_swo.data->>'status'), '') as "Status",
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