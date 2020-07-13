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
#Update Site

table = "sites"

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

#_____________
#Update Tenant

table = "tenants"

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
 ( b_tenants.embedded = false OR b_tenants.embedded is null)
 """

#postgre_to_mysql.rebuildFromQuery(postConn,mysqlConn,table,postQuery)
#postgre_to_mysql.createFromQuery(postConn,mysqlConn,table,postQuery)
postgre_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)

#_____________
#Update Customer requests

table = "customer_requests"

postQuery = """select
  b_requests.data->>'site_id_text' as "Site ID",
  b_requests.data->'request_id' ->>'prefix' as "CAR ID - prefix",
  b_requests.data->'request_id' ->>'number' as "CAR ID - number",
  CONCAT(b_requests.data->'request_id' ->>'prefix', '-',b_requests.data->'request_id' ->>'number') AS "CAR ID",
  b_requests.data->>'requestor' as "Operator",  
  b_requests.data->>'tenant_id' as "Tenant ID",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 37 AND field_id = '19' AND option_id = b_requests.data->>'tenant_configuration'), '') as "Configuration",
  b_requests.data->'nominal_coordinates'->>'x' as "Nominal coordinates - Latitude - WGS 84",
  b_requests.data->'nominal_coordinates'->>'y' as "Nominal coordinates - Longitude - WGS 84",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 52 AND value_id = b_requests.data->>'request_type'), '') as "Request type",
  b_requests.data->>'program_id_number' as "Program ID",
  b_requests.data->>'program_id' as "Program", 
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 76 AND value_id = b_requests.data->>'sow'), '') as "SOW",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_requests.data->>'request_date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Request date",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_requests.data->>'requested_rfi','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Expected RFI",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_requests.data->>'date_of_completion','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Date of completion",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_requests.data->>'rinternal_rfi','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Internal RFI",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_requests.data->>'expected_end_work','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Expected end work",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 37 AND field_id = '12' AND option_id = b_requests.data->>'status'), '') as "CR status",
  b_requests.data->'project_id' ->>'prefix' as "Prj ID - prefix",
  b_requests.data->'project_id' ->>'number' as "Prj ID - number",
  CONCAT(b_requests.data->'project_id' ->>'prefix', '-',b_requests.data->'project_id' ->>'number') AS "Prj ID",  
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 37 AND field_id = '13' AND option_id = b_requests.data->>'final_validation'), '') as "Final validation",
  b_requests.data->>'comment_final' as "Comment",  
  b_requests.data->>'cost' as "Cost",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 37 AND field_id = '52' AND option_id = b_requests.data->>'cost_share_scheme'), '') as "RTR-STR Cost Share Scheme",
  b_requests.data->>'final_validation_b2s' as "Decision",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 37 AND field_id = '31' AND option_id = b_requests.data->>'need_rtr'), '') as "Need RTR",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 37 AND field_id = '32' AND option_id = b_requests.data->>'need_str'), '') as "Need STR",
  b_requests.data->>'need_structural_calculation' as "Need structural analysis",
  b_requests.data->>'tower_extension_required' as "Tower extension required",
  b_requests.data->>'need_power_upgrade' as "Need power upgrade",
  b_requests.data->>'additional_average_power_consumption' as "Additional Average power consumption",
  b_requests.data->>'additional_peak_power_consumption' as "Additional Peak power consumption",
  b_requests.data->>'total_average_power_consumption' as "Total Average power consumption",
  b_requests.data->>'total_peak_power_consumption' as "Total Peak power consumption",
  b_requests.data->>'search_radius' as "Search radius",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 76 AND value_id = b_requests.data->>'location_classification'), '') as "Location Classification",
  b_requests.data->>'planned_tower_height' as "Customer Planned Tower Height",
  b_requests.data->>'nominal_objective' as "Nominal Objective",
  b_requests.data->>'zone_type' as "Zone Type",
  b_requests.data->>'critical_site' as "Critical Site",
  b_requests.data->>'decision_rtr' as "Decision RTR",
  b_requests.data->>'decision_str' as "Decision STR",
  b_requests.data->>'author' as "Request by",
  b_requests.data->>'request_id' as "Space management and Structural"
  FROM forms_data as b_requests
 WHERE b_requests.form_id in (37) AND 
  b_requests.enabled  = true AND 
 ( b_requests.embedded = false OR b_requests.embedded is null)
 """

#postgre_to_mysql.rebuildFromQuery(postConn,mysqlConn,table,postQuery)
#postgre_to_mysql.createFromQuery(postConn,mysqlConn,table,postQuery)
postgre_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)

table = "users"

postQuery = """select
  b_teams.data->>'username' as "system_name",
  CONCAT('["',b_teams.data->>'username','"]') AS "system_name2",
  b_teams.data->>'loginName' as "Login name",
  b_teams.data->>'firstname' as "First name",
  b_teams.data->>'lastname' as "Last name"
 FROM forms_data as b_teams 
 WHERE b_teams.form_id in (1) AND 
  b_teams.enabled  = true AND 
 ( b_teams.embedded = false OR b_teams.embedded is null)
 """

#postgre_to_mysql.rebuildFromQuery(postConn,mysqlConn,table,postQuery)
#postgre_to_mysql.createFromQuery(postConn,mysqlConn,table,postQuery)
postgre_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)

table = "teams"

postQuery = """select
  b_teams.data->>'system_name' as "system_name",
  CONCAT('["',b_teams.data->>'system_name','"]') AS "system_name2",
  b_teams.data->>'team_name' as "Team name"
 FROM forms_data as b_teams 
 WHERE b_teams.form_id in (4) AND 
  b_teams.enabled  = true AND 
 ( b_teams.embedded = false OR b_teams.embedded is null)
 """

#postgre_to_mysql.rebuildFromQuery(postConn,mysqlConn,table,postQuery)
#postgre_to_mysql.createFromQuery(postConn,mysqlConn,table,postQuery)
postgre_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)


table = "cr_approval_matrix"

postQuery = """select
  b_approval.data->'request_id' ->>'prefix' as "CAR ID - prefix",
  b_approval.data->'request_id' ->>'number' as "CAR ID - number",
  CONCAT(b_approval.data->'request_id' ->>'prefix', '-',b_approval.data->'request_id' ->>'number') AS "CAR ID",
  b_approval.data->>'approved_by' as "Team",
  b_approval.data->>'team' as "Team1",
  b_approval.data->>'approving' as "Approving",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 22 AND field_id = '2' AND option_id = b_approval.data->>'decision'), '') as "Decision",
  b_approval.data->>'comment' as "Comment"
  FROM forms_data as b_approval 
 WHERE b_approval.form_id in (22) AND 
  b_approval.enabled  = true AND 
 ( b_approval.embedded = false OR b_approval.embedded is null)
 """

#postgre_to_mysql.rebuildFromQuery(postConn,mysqlConn,table,postQuery)
#postgre_to_mysql.createFromQuery(postConn,mysqlConn,table,postQuery)
postgre_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)

table = "cos_report_cr_comments"

postQuery = """select  
  CASE WHEN (b_customer_request.data->>'request_id' != '')  THEN (  CASE  WHEN (b_customer_request.data->'request_id'->>'draft' = 'true')  THEN (b_customer_request.data->'request_id'->>'draft_number')  WHEN (b_customer_request.data->'request_id'->>'number' != '')  THEN ( CONCAT(  CASE  WHEN ( b_customer_request.data->'request_id'->>'prefix' != '')  THEN ( b_customer_request.data->'request_id'->>'prefix' )  ELSE '' END  , '-',  CASE  WHEN ( LENGTH(b_customer_request.data->'request_id'->>'number') > 4)  THEN ( b_customer_request.data->'request_id'->>'number')  ELSE ( LPAD(b_customer_request.data->'request_id'->>'number', 4, '0') )  END  ) )  ELSE '' END  ) ELSE '' END  AS "CAR ID" ,
  r_cr_contain_comment_remark.data->>'internal_detail_of_issue' as "Comment",
  CASE WHEN (r_cr_contain_comment_remark.data->>'remark_id' != '')  THEN (  CASE  WHEN (r_cr_contain_comment_remark.data->'remark_id'->>'draft' = 'true')  THEN (r_cr_contain_comment_remark.data->'remark_id'->>'draft_number')  WHEN (r_cr_contain_comment_remark.data->'remark_id'->>'number' != '')  THEN ( CONCAT(  CASE  WHEN ( r_cr_contain_comment_remark.data->'remark_id'->>'prefix' != '')  THEN ( r_cr_contain_comment_remark.data->'remark_id'->>'prefix' )  ELSE '' END  , '-',  CASE  WHEN ( LENGTH(r_cr_contain_comment_remark.data->'remark_id'->>'number') > 4)  THEN ( r_cr_contain_comment_remark.data->'remark_id'->>'number')  ELSE ( LPAD(r_cr_contain_comment_remark.data->'remark_id'->>'number', 4, '0') )  END  ) )  ELSE '' END  ) ELSE '' END  AS "Comment ID" , 
  TO_CHAR(TO_TIMESTAMP(( NULLIF(r_cr_contain_comment_remark.data->>'date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Date",
  (select ((d.data ->> 'firstname'::text) || ' '::text || (d.data ->> 'lastname'::text)) from forms_data d where d.enabled and d.form_id = 1 and d.id = (r_cr_contain_comment_remark.data->>'raised_by')::text) AS "Raised by"
 FROM forms_data as b_customer_request 
 left join forms_relations_data as r0 on r0.relation_id = 67 and (r0.source_id = b_customer_request.id or r0.target_id = b_customer_request.id ) and r0.enabled = true 
 left join forms_data as r_cr_contain_comment_remark on (r_cr_contain_comment_remark.id = r0.source_id or r_cr_contain_comment_remark.id =r0.target_id ) and r_cr_contain_comment_remark.form_id = 80 
 WHERE b_customer_request.form_id in (37) AND b_customer_request.enabled  = true AND ( b_customer_request.embedded = false OR b_customer_request.embedded is null)
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
val = ("run.py", start_time, end_time)
mycursor.execute(sql, val)

mysqlConn.commit()