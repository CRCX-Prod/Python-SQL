import psycopg2
import mysql_module
import postgre_module

postgreQuery = """Select
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
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 97 AND field_id = '3' AND option_id = b_tenants.data->>'tenant_status'), '') as "Tenant status",
  b_tenants.data->>'tenant_class' as "Tenant class"
 FROM forms_data as b_tenants 
 WHERE b_tenants.form_id in (97) AND 
  b_tenants.enabled  = true AND 
 ( b_tenants.embedded = false OR b_tenants.embedded is null) AND 
 ((b_tenants.data ->>'entity') IN ('2'))"""

postgreConn = psycopg2.connect(
    host="192.168.1.16", 
    port = 5432, 
    database="report_db_apollo_towers", 
    user="datawarehouse", 
    password="HPdhyHCYc8SfLY05EZKOSeH1ekoMXgzZuf44d4gP"
    )

#mysql_module.connection ()

queryColumns = postgre_module.getColumns (postgreConn,postgreQuery)

queryData = postgre_module.getData (postgreConn,postgreQuery)

print(queryData)

postgreConn.close()