
#MySQL connection
import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.1.153",
  user="admin",
  passwd="P@ssw0rd",
  database="00_cos_warehouse"
)

print(mydb)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb) 


 [('BAW5542', 'PBAG00119', '2', '["ROLE_TEAM_OREEDOO"]', 'Anchor', '', None, None, '17.34292', '96.4571', 'Class C', 'Tower + Power', 'On air', '3'), ('KCN00411', '1-01-01004-010', '2', '["ROLE_TEAM_MPT"]', 'Colocation', '', None, None, '26.69798', '96.20745', 'Class A', 'Tower + Power', 'On air', '1'), ('MDY0235', 'PMDY00188', '2', '["ROLE_TEAM_MYTEL"]', 'Colocation', '', None, None, '21.89774', '96.13383', '', 'Tower + Power', 'New appl.', None), ('CHN00119', '1-01-05030-014', '2', '["ROLE_TEAM_MPT"]', 'Colocation', '', None, None, '23.80442', '94.14537', '', 'Tower only', 'On air', None), ('AWD00235', '1-01-17015-002', '2', '["ROLE_TEAM_MPT"]', 'Colocation', '', None, None, '16.76274', '95.18961', 'Class A', 'Tower + Power', 'On air', '1'), ('AYY0074', '1-01-17001-001', '2', '["ROLE_TEAM_MYTEL"]', 'Colocation', '', None, None, '16.75889', '94.72659', '', 'Tower only', 'On air', None), ('AYW5101', '1-01-17014-004', '2', '["ROLE_TEAM_OREEDOO"]', 'Anchor', '', None, None, '16.49199', '94.96466', 'Class B', 'Tower + Power', 'On air', '2'), ('TAW6111', 'PTNT00302', '2', '["ROLE_TEAM_OREEDOO"]', 'Anchor', '', None, None, '12.42841', '98.60935', 'Class C', 'Tower + Power', 'On air', '3'), ('KC0604', '1-01-01010-002', '2', '["ROLE_TEAM_TELENOR"]', 'Colocation', '', None, None, '24.0236', '97.15739', '', 'Tower only', 'On air', None), ('MG1146', '1-01-09021-008', '2', '["ROLE_TEAM_TELENOR"]', 'Colocation', '', None, None, '21.57468', '94.60768', '', 'Tower only', 'On air', None), ('SAW0419', '1-01-05001-009', '2', '["ROLE_TEAM_OREEDOO"]', 'Anchor', '', None, None, '21.88594', '95.97668', 'Class B', 'Tower + Power', 'On air', '2'), ('SAW0222', '1-01-05001-006', '2', '["ROLE_TEAM_OREEDOO"]', 'Anchor', '', None, None, '22.14853', '95.88752', 'Class B', 'Tower + Power', 'On air', '2'), ('AYW5019', '1-01-17013-005', '2', '["ROLE_TEAM_OREEDOO"]', 'Anchor', '', None, None, '17.81222', '95.27023', 'Class B', 'Tower + Power', 'On air', '2'), ('KA3562', '1-01-03005-008', '2', '["ROLE_TEAM_TELENOR"]', 'Colocation', '', None, None, '16.69008', '98.46425', '', 'Tower only', 'On air', None), ('AWD00548', '1-01-17008-022', '2', '["ROLE_TEAM_MPT"]', 'Colocation', '', None, None, '17.72623', '95.4047', 'Class B', 'Tower + Power', 'On air', '2'), ('KYH0109', '1-01-02002-003', '2', '["ROLE_TEAM_MYTEL"]', 'Colocation', '', None, None, '19.57796', '96.99248', '', 'Tower + Power', 'New appl.', None)]


# Postgre connection
import psycopg2

# Establish a connection to the database by creating a cursor object
# conn = psycopg2.connect("dbname=suppliers port=5432 user=postgres password=postgres")

# Or:
conn = psycopg2.connect(host="192.168.1.16", port = 5432, database="report_db_apollo_towers", user="datawarehouse", password="HPdhyHCYc8SfLY05EZKOSeH1ekoMXgzZuf44d4gP")

# Create a cursor object
cur = conn.cursor()

# A sample query of all data from the "vendors" table in the "suppliers" database
cur.execute("""Select
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
 ((b_tenants.data ->>'entity') IN ('2'))""")
query_results = cur.fetchall()


#other query
## cur.execute("""select json_configuration ->>'form_fields' from forms
## where forms.id in (97)""")
## query_results = cur.fetchall()


#print(query_results)

#query_columns = cur.description(0)
query_columns = [desc[0] for desc in cur.description]

print(query_columns)

# Close the cursor and connection to so the server can allocate bandwidth to other requests

cur.close()
conn.close()

mysql_module.insertData(queryColumns,2,3)