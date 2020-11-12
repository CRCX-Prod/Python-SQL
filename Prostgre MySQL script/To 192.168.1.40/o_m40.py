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

#___________
#Update Power sources

table = "power_sources"

postQuery = """select 
  b_sources.data->'power_source_id' ->>'prefix' as "Power source ID - prefix",
  b_sources.data->'power_source_id' ->>'number' as "Power source ID  - number",
  b_sources.data->'power_source_id' ->>'number' as "Power source ID",
  b_sources.data->>'anchor_id' as "Anchor ID",
  b_sources.data->>'site_id_text' as "Site ID",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 71 AND field_id = '25' AND option_id = b_sources.data->>'source_test'), '') as "Source type",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 71 AND field_id = '22' AND option_id = b_sources.data->>'status'), '') as "Status",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_sources.data->>'connection_date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Connection",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_sources.data->>'last_installation','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Last installation",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_sources.data->>'connection_f','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Forecast",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_sources.data->>'source_dismantled','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Source dismantled",
  b_sources.data->>'dg_brand' as "DG brand",
  b_sources.data->>'dg_capacity' as "DG capacity",
  b_sources.data->>'dg_running_hour' as "DG Running hour",
  b_sources.data->>'idg_cph' as "DG CPH",
  b_sources.data->>'ac_dc_dg' as "AC-DC DG",
  b_sources.data->>'ats' as "ATS",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 71 AND field_id = '46' AND option_id = b_sources.data->>'new_used_asset'), '') as "New-Used Asset",
  b_sources.data->>'dg_2_brand' as "DG 2 brand",
  b_sources.data->>'dg_2_capacity' as "DG 2 capacity",
  b_sources.data->>'dg_2_running_hours' as "DG 2 running hours",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 71 AND field_id = '69' AND option_id = b_sources.data->>'new_used_asset_dg_2'), '') as "New-Used Asset DG 2",   
  b_sources.data->>'ac_dc_dg_2' as "AC-DC DG 2",
  b_sources.data->>'battery_brand' as "Battery Brand",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 71 AND field_id = '51' AND option_id = b_sources.data->>'battery_type'), '') as "Battery type",   
  b_sources.data->>'battery_capacity' as "Battery Capacity",
  b_sources.data->>'battery_voltage' as "Battery voltage",
  b_sources.data->>'battery_capacity_string' as "Battery capacity per string",
  b_sources.data->>'no_of_strings' as "No of strings",
  b_sources.data->>'rectifier_type' as "Rectifier Type",
  b_sources.data->>'rectifier_capacity_unit' as "Rectifier capacity per unit",
  b_sources.data->>'working_rectifier' as "Working Rectifier",
   b_sources.data->>'power_cabinet_brand' as "Power Cabinet Brand",
  b_sources.data->>'power_cabinet_capacity' as "Power Cabinet Capacity",   
  b_sources.data->>'rms_status' as "RMS Status",
  b_sources.data->>'rms_system' as "RMS System",
  b_sources.data->>'sim_number' as "Sim number",
  b_sources.data->>'sim_operator' as "Sim operator",
  b_sources.data->>'pe_vendor' as "PE vendor",
  b_sources.data->>'pe_type' as "PE type",
  b_sources.data->>'pe_system_capacity' as "PE system capacity",
  b_sources.data->>'dg_fuel_tank' as "No DG & Fuel tank",
  b_sources.data->>'meter_id' as "Meter ID",
  b_sources.data->>'cable_distance' as "Cable distance",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 71 AND field_id = '59' AND option_id = b_sources.data->>'grid_installation_type'), '') as "Grid installation type",     
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 71 AND field_id = '23' AND option_id = b_sources.data->>'permenant'), '') as "Grid status",   
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_sources.data->>'last_change','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Last change"  
  FROM forms_data as b_sources
 WHERE b_sources.form_id in (71) AND 
  b_sources.enabled  = true AND 
 ( b_sources.embedded = false OR b_sources.embedded is null)
 """

#postgre_to_mysql.rebuildFromQuery(postConn,mysqlConn,table,postQuery)
#postgre_to_mysql.createFromQuery(postConn,mysqlConn,table,postQuery)
postgre_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)


#__________
#Record logrm 

now = datetime.now()

end_time = now.strftime("20%y-%m-%d %H:%M:%S")
print("End at ", end_time)

mycursor = mysqlConn.cursor()

sql = "INSERT INTO 00_log_script (script_name, start, end) VALUES (%s, %s, %s)"
val = ("o_m.py", start_time, end_time)
mycursor.execute(sql, val)

mysqlConn.commit()