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
    host="192.168.1.153",
    user="admin",
    passwd="P@ssw0rd",
    database="00_python"
    )

#___________
#Update O&M actions

table = "o_m_actions"

postQuery = """select 
  b_actions.data->'action_id' ->>'prefix' as "Action ID - prefix",
  b_actions.data->'action_id' ->>'number' as "Action ID  - number",
  b_actions.data->'action_id' ->>'number' as "Action ID",
  b_actions.data->>'anchor_id' as "Anchor ID",
  b_actions.data->>'site_id_text' as "Site ID",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 32 AND value_id = b_actions.data->>'entity'), '') as "Entity",
  b_actions.data->>'zone_team' as "Zone",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 63 AND value_id = b_actions.data->>'anchor_class'), '') as "Anchor class",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 63 AND value_id = b_actions.data->>'power_configuration'), '') as "Power configuration",
  b_actions.data->>'week' as "Week",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_actions.data->>'date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Open date",
  b_actions.data->>'week_raw_sla' as "Week raw SLA",
  b_actions.data->>'repetitive_outages' as "Repetitive outages",
  b_actions.data->>'most_frequent_rca' as "RCA",
  b_actions.data->>'rca_sub_category' as "RCA sub category",
  b_actions.data->>'rca_summary' as "RCA summary",
  b_actions.data->>'battery_backup_duration' as "Battery backup duration",
  b_actions.data->>'grid_outage_duration' as "Grid outage duration",  
  b_actions.data->>'action_plan' as "Action plan",
  b_actions.data->>'action_by' as "Action by",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_actions.data->>'action_due','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Action due",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 120 AND field_id = '13' AND option_id = b_actions.data->>'status'), '') as "Status",
  b_actions.data->>'created_by' as "Created by"
 FROM forms_data as b_actions
 WHERE b_actions.form_id in (120) AND 
  b_actions.enabled  = true AND 
 ( b_actions.embedded = false OR b_actions.embedded is null)
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
val = ("o_m.py", start_time, end_time)
mycursor.execute(sql, val)

mysqlConn.commit()