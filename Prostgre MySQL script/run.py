import psycopg2
import mysql.connector
import postgre_to_mysql

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
#Update Site

table = "site_test"

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
 ( b_sites.embedded = false OR b_sites.embedded is null) AND 
 ((b_sites.data ->>'entity') IN ('2'))
 """

postgre_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)

#_____________
#Update Tenant

table = "tenants_test"

postQuery = """Select
  b_tenants.data->>'tenant_site_id' as "Tenant ID",
  b_tenants.data->>'site_id_text' as "Site ID", 
  b_tenants.data->>'entity' as "Entity",  
  b_tenants.data->>'operator' as "Tenant",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 97 AND field_id = '15' AND option_id = b_tenants.data->>'tenant_type'), '') as "Tenant type",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 97 AND field_id = '33' AND option_id = b_tenants.data->>'power'), '') as "Power model tenant",
  b_tenants.data->>'power_type' as "Billable power",
  b_tenants.data->>'power_provider' as "Power provider",
  b_tenants.data->'coordinates'->>'x' as "Latitude",
  b_tenants.data->'coordinates'->>'y' as "Longitude",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 63 AND value_id = b_tenants.data->>'tenant_class'), '') as "Tenant class" ,
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 97 AND field_id = '26' AND option_id = b_tenants.data->>'tenant_configuration'), '') as "Tenant configuration",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 97 AND field_id = '3' AND option_id = b_tenants.data->>'tenant_status'), '') as "Tenant status"
 FROM forms_data as b_tenants 
 WHERE b_tenants.form_id in (97) AND 
  b_tenants.enabled  = true AND 
 ( b_tenants.embedded = false OR b_tenants.embedded is null) AND 
 ((b_tenants.data ->>'entity') IN ('2'))
 """

postgre_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)
