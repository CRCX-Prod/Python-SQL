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

postQuery = """Select
  b_sites.data->>'site_id_text' as "Site ID" ,
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 32 AND value_id = b_sites.data->>'entity'), '') as "Entity" ,
  b_sites.data->>'zone_team' as "Zone" ,
  b_sites.data->>'anchor_id' as "Anchor ID" ,
  b_sites.data->>'anchor_tenant' as "Anchor operator" ,
  b_sites.data->>'tenancy_on_air' as "Tenancy on air" ,
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 63 AND value_id = b_sites.data->>'anchor_class'), '') as "Anchor class" ,
  b_sites.data->>'tower_height' as "Height" ,
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 80 AND value_id = b_sites.data->>'site_category'), '') as "Site category" , 
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 90 AND field_id = '134' AND option_id = b_sites.data->>'asset_status'), '') as "Asset status",
  b_sites.data->>'site_notes' as "Site notes" ,
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 90 AND field_id = '92' AND option_id = b_sites.data->>'site_tier'), '') as "Site tier",
  b_sites.data->'coordinates_site'->>'x' as "Latitude",
  b_sites.data->'coordinates_site'->>'y' as "Longitude",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 90 AND field_id = '103' AND option_id = b_sites.data->>'colocation_potential'), '') as "Colocation potential" ,
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 90 AND field_id = '114' AND option_id = b_sites.data->>'community_status'), '') as "Community status", 
  b_sites.data->>'fdn_stress' as "FDN stress" ,
  b_sites.data->>'power_configuration' as "Power configuration" ,
  b_sites.data->>'twr_stress' as "TWR stress" ,
  b_sites.data->>'region_state' as "Region/State" ,
  b_sites.data->>'division' as "Division" ,
  b_sites.data->>'district' as "District" ,
  b_sites.data->>'township' as "Township" ,
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_sites.data->>'site_built','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Site ready date" ,
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_sites.data->>'tower_dismantled','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Tower dismantled" ,
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_sites.data->>'power_dismantled','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Power dismantled" ,
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_sites.data->>'ground_lease_terminated','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Ground lease terminated" ,
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_sites.data->>'site_dismantled','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Site end date" ,
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 8 AND value_id = b_sites.data->>'aera_type'), '') as "Area type"
 FROM forms_data as b_sites 
 WHERE b_sites.form_id in (90) AND 
  b_sites.enabled  = true AND 
 ( b_sites.embedded = false OR b_sites.embedded is null)
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