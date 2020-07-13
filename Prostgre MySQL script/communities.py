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
#Update Community issues

table = "community_issues"

postQuery = """select
  b_community.data->>'site_id' as "Site ID",
  b_community.data->'issue_id' ->>'prefix' as "Issue ID - prefix",
  b_community.data->'issue_id' ->>'number' as "Issue ID  - number",
  CONCAT(b_community.data->'issue_id' ->>'prefix', '-',b_community.data->'issue_id' ->>'number') AS "Issue ID",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_community.data->>'open_date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Open date",
  (select ((d.data ->> 'firstname'::text) || ' '::text || (d.data ->> 'lastname'::text)) from forms_data d where d.enabled and d.form_id = 1 and d.id = (b_community.data->>'opened_by')::text) AS "Opened by",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 37 AND value_id = b_community.data->>'category'), '') as "Category",
  b_community.data->>'issue_description' as "Issue description",
  b_community.data->>'resolution_cost' as "Resolution cost",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 23 AND value_id = b_community.data->>'currency'), '') as "Currency",
  b_community.data->>'site_down' as "Site down",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_community.data->>'closed_date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Closed date",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_community.data->>'ptd_involved','') )::bigint/1000) , 'YYYY-MM-DD')::text as "PTD involved",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_community.data->>'regional_government_involved','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Regional government involved",
  b_community.data->>'address' as "Address",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 50 AND field_id = '12' AND option_id = b_community.data->>'status'), '') as "Status"
 FROM forms_data as b_community
 WHERE b_community.form_id in (50) AND 
  b_community.enabled  = true AND 
 ( b_community.embedded = false OR b_community.embedded is null)
 """

#postgre_to_mysql.rebuildFromQuery(postConn,mysqlConn,table,postQuery)
#postgre_to_mysql.createFromQuery(postConn,mysqlConn,table,postQuery)
postgre_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)


#___________
#Update Comments

table = "comments"

postQuery = """select
  b_comment.data->>'site_id' as "Site ID",
  b_comment.data->'remark_id' ->>'prefix' as "Comment ID - prefix",
  b_comment.data->'remark_id' ->>'number' as "Comment ID  - number",
  CONCAT(b_comment.data->'remark_id' ->>'prefix', '-',b_comment.data->'remark_id' ->>'number') AS "Comment ID",
  b_comment.data->'issue_id' ->>'prefix' as "Issue ID - prefix",
  b_comment.data->'issue_id' ->>'number' as "Issue ID  - number",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_comment.data->>'date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Date",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 37 AND value_id = b_comment.data->>'category'), '') as "Category",
  b_comment.data->>'internal_detail_of_issue' as "Comment",
  (select ((d.data ->> 'firstname'::text) || ' '::text || (d.data ->> 'lastname'::text)) from forms_data d where d.enabled and d.form_id = 1 and d.id = (b_comment.data->>'raised_by')::text) AS "Raised by"
 FROM forms_data as b_comment 
  WHERE b_comment.form_id in (80) AND 
  b_comment.enabled  = true AND 
 ( b_comment.embedded = false OR b_comment.embedded is null)
 """

#postgre_to_mysql.rebuildFromQuery(postConn,mysqlConn,table,postQuery)
#postgre_to_mysql.createFromQuery(postConn,mysqlConn,table,postQuery)
postgre_to_mysql.repopulateFromQuery(postConn,mysqlConn,table,postQuery)

#___________
#Update Restrictions

table = "restrictions"

postQuery = """select
  b_restriction.data->>'site_pat' as "Site ID",
  b_restriction.data->'restriction_id' ->>'prefix' as "Restriction ID - prefix",
  b_restriction.data->'restriction_id' ->>'number' as "Restriction  ID  - number",
  b_restriction.data->'restriction_id' ->>'number' as "Restriction  ID",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 83 AND field_id = '4' AND option_id = b_restriction.data->>'restriction_type'), '') as "Restriction type",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 83 AND field_id = '13' AND option_id = b_restriction.data->>'restriction_status'), '') as "Restriction status",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_restriction.data->>'restriction_implementation_date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Restriction implementation date",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_restriction.data->>'restriction_removed','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Restriction removed",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 83 AND field_id = '10' AND option_id = b_restriction.data->>'can_dg_be_used_if_grid'), '') as "Can DG be used if Grid is Down",
  b_restriction.data->>'restriction_start_time' as "Restriction start time",  
  b_restriction.data->>'restriction_end_time' as "Restriction end time",
  b_restriction.data->>'restriction_duration' as "Restriction duration"
 FROM forms_data as b_restriction 
  WHERE b_restriction.form_id in (83) AND 
  b_restriction.enabled  = true AND 
 ( b_restriction.embedded = false OR b_restriction.embedded is null)
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
val = ("communities.py", start_time, end_time)
mycursor.execute(sql, val)

mysqlConn.commit()