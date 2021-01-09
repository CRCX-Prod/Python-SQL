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
#Update Tower structure

table = "tower_structure"

postQuery = """select b_structure.data->>'site_id' as "Site ID",
  b_structure.data->'tower_id' ->>'prefix' as "Tower ID - prefix",
  b_structure.data->'tower_id' ->>'number' as "Tower ID - number",
  CONCAT(b_structure.data->'tower_id' ->>'prefix',TO_CHAR((b_structure.data->'tower_id' ->>'number')::bigint, '0000')::text) as "Tower ID",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 40 AND value_id = b_structure.data->>'location_type'), '') as "Site type",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 68 AND value_id = b_structure.data->>'type_of_structure'), '') as "Structure type",
  b_structure.data->>'structure_type_for_others_only' as "Structure type for others only",
  b_structure.data->>'operation_code' as "Tower model",
  b_structure.data->>'tower_height' as "Height",
  b_structure.data->>'building_height' as "Height - Building",
  b_structure.data->>'design_height' as "Height - Design",
  b_structure.data->>'height_-_extension' as "Height - Extension",
  b_structure.data->>'height_-_reduction' as "Height - Reduction",
  b_structure.data->>'design_epa' as "Capacity - Design",
  b_structure.data->>'capacity_-_structural' as "Capacity - Structural",
  b_structure.data->>'wind_load_installed' as "Capacity - Installed",
  b_structure.data->>'wind_load_available' as "Capacity - Available",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 75 AND value_id = b_structure.data->>'active_wind_zone'), '') as "Wind speed - Active",  
  b_structure.data->>'new_wind_zone' as "Wind Zone - New",
  b_structure.data->>'old_wind_zone' as "Wind Zone - Old",
  b_structure.data->>'design_wind_speed' as "Design wind speed",
  b_structure.data->>'crest_height' as "Crest height",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 100 AND field_id = '43' AND option_id = b_structure.data->>'topographic_category'), '') as "Topographic category",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 100 AND field_id = '44' AND option_id = b_structure.data->>'exposure_category'), '') as "Exposure category",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 100 AND field_id = '45' AND option_id = b_structure.data->>'structure_class'), '') as "Structure class",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 100 AND field_id = '31' AND option_id = b_structure.data->>'foundation_design'), '') as "Foundation type",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 100 AND field_id = '57' AND option_id = b_structure.data->>'fdn_design_type'), '') as "Foundation sub type",
  b_structure.data->>'foundation_base_depth' as "Foundation base depth",
  b_structure.data->>'ground_water_depth' as "Ground Water Depth",
  b_structure.data->>'submerged_ratio' as "Submerged ratio",
  b_structure.data->>'flood_history' as "Flood history",
  b_structure.data->>'custom_foundation' as "Custom foundation",
  b_structure.data->>'aviation_approved_height' as "Aviation Applied and Approved Height",
  b_structure.data->>'aviation_restricted_height' as "Aviation Restricted Max Height",
  b_structure.data->>'civil_work_vendor' as "Civil work vendor",
  b_structure.data->>'manufacture_name' as "Manufacturer",
  b_structure.data->'index_calculation' ->>'prefix' as "A - index - Calculation - prefix",
  b_structure.data->'index_calculation' ->>'number' as "A - index - Calculation - number",
  CONCAT(b_structure.data->'index_calculation' ->>'prefix', '-',b_structure.data->'index_calculation' ->>'number') as "A - index - Calculation"
  FROM forms_data as b_structure
 WHERE b_structure.form_id in (100) AND 
  b_structure.enabled  = true AND 
 ( b_structure.embedded = false OR b_structure.embedded is null)
 """

#postgre_to_mysql.rebuildFromQuery(postConn,mysqlConn,table,postQuery)
#postgre_to_mysql.createFromQuery(postConn,mysqlConn,table,postQuery)
postgre_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)

#___________
#Update Item structural analysis

table = "item_structural_analysis"

postQuery = """select b_itemstructural.data->'analyse_id'->>'number' as "Analysis ID",
  b_itemstructural.data->'item_t_key'->>'number' as "Item key",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 62 AND value_id = b_itemstructural.data->>'item'), '') as "Item",
  b_itemstructural.data->>'value' as "Value"
 FROM forms_data as b_itemstructural
 WHERE b_itemstructural.form_id in (95) AND 
  b_itemstructural.enabled  = true AND 
 ( b_itemstructural.embedded = false OR b_itemstructural.embedded is null)
 """

#postgre_to_mysql.rebuildFromQuery(postConn,mysqlConn,table,postQuery)
#postgre_to_mysql.createFromQuery(postConn,mysqlConn,table,postQuery)
postgre_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)

#___________
#Update Item foundation analysis

table = "item_foundation_analysis"

postQuery = """select b_itemfoundation.data->'analyse_id'->>'number' as "Analysis ID",
  b_itemfoundation.data->'item_a_key'->>'number' as "Item A key",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 35 AND value_id = b_itemfoundation.data->>'item'), '') as "Item",
  b_itemfoundation.data->>'value' as "Value"
 FROM forms_data as b_itemfoundation
 WHERE b_itemfoundation.form_id in (56) AND 
  b_itemfoundation.enabled  = true AND 
 ( b_itemfoundation.embedded = false OR b_itemfoundation.embedded is null)
 """

#postgre_to_mysql.rebuildFromQuery(postConn,mysqlConn,table,postQuery)
#postgre_to_mysql.createFromQuery(postConn,mysqlConn,table,postQuery)
postgre_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)

#___________
#analysis

table = "analysis"

postQuery = """select b_analysis.data->>'site_id' as "Site ID",
  b_analysis.data->'analyse_id' ->>'number' as "Analysis ID",
  b_analysis.data->'request_id' ->>'prefix' as "CAR ID - prefix",
  b_analysis.data->'request_id' ->>'number' as "CAR ID - number",
  CONCAT(b_analysis.data->'request_id' ->>'prefix', '-',b_analysis.data->'request_id' ->>'number') AS "CAR ID",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 54 AND field_id = '99' AND option_id = b_analysis.data->>'type_of_analysis'), '') as "Analysis type",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 54 AND field_id = '102' AND option_id = b_analysis.data->>'scope_of_analysis'), '') as "Analysis scope",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_analysis.data->>'analysis_date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Analysis date",
  b_analysis.data->>'analysis_set' as "Analysis set",
  b_analysis.data->>'additional_capacity' as "Additional capacity",
  b_analysis.data->>'objective_stress' as "Objective stress",
  b_analysis.data->>'analysis_wind_speed' as "Analysis wind speed",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 54 AND field_id = '2' AND option_id = b_analysis.data->>'max_stress_color'), '') as "Max stress color",
  b_analysis.data->>'max_stress_value' as "Max stress (%)",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 54 AND field_id = '106' AND option_id = b_analysis.data->>'status'), '') as "Status",
  b_analysis.data->>'struct_company_gbt' as "Company name",
  b_analysis.data->>'overturn_stability' as "Overturn stability (%)",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 54 AND field_id = '2' AND option_id = b_analysis.data->>'overturn_stability_color'), '') as "Overturn stability Color",
  b_analysis.data->>'new_wind_zone' as "New Wind zone",
  b_analysis.data->>'old_wind_zone' as "Old Wind zone",
  b_analysis.data->>'active_wind_zone' as "Active Wind zone",
  b_analysis.data->>'location_type' as "Site type",
  b_analysis.data->>'design_wind_speed' as "Design Wind speed",
  b_analysis.data->>'struct_engineer' as "Struct Engineer",
  b_analysis.data->>'eq_slab_size_m_x_m' as "EQ Slab Size (m x m)",
  b_analysis.data->>'width_eq_slab' as "EQ Slab Width",
  b_analysis.data->>'lenght_eq_slab' as "EQ Slab Lenght",
  b_analysis.data->>'eq_slab_height_m' as "EQ Slab Height",
  b_analysis.data->>'eq_slab_count' as "EQ Slab Count",
  b_analysis.data->>'concrete_estimation' as "Concrete Vol Estimate",
  b_analysis.data->>'steel_weight' as "Steel Weight Estimate",
  b_analysis.data->>'flood_history' as "Flood history",
  b_analysis.data->>'soil_fos' as "Soil FoS",
  b_analysis.data->>'allowable_sbc' as "Allowable SBC",
  b_analysis.data->>'ground_water_depth' as "Ground water depth",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 119 AND field_id = '2' AND option_id = b_analysis.data->>'existing_building_analysis_ba'), '') as "Existing Building Analysis (BA)",
  b_analysis.data->>'strengthening_count' as "Strengthening Count",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_analysis.data->>'last_update','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Last update"
 FROM forms_data as b_analysis
 WHERE b_analysis.form_id in (54) AND 
  b_analysis.enabled  = true AND 
 ( b_analysis.embedded = false OR b_analysis.embedded is null)
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
val = ("structural.py", start_time, end_time)
mycursor.execute(sql, val)

mysqlConn.commit()