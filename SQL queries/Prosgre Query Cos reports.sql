%___________________________________________________________________________
%sites
%___________________________________________________________________________

table = "sites"

Select
  b_sites.data->>'site_id_text' as "Site ID" ,
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 32 AND value_id = b_sites.data->>'entity'), '') as "Entity",
  b_sites.data->>'zone_team' as "Zone" ,
  b_sites.data->>'anchor_id' as "Anchor ID" ,
  b_sites.data->>'anchor_tenant' as "Anchor operator" ,
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 40 AND value_id = b_sites.data->>'typology'), '') as "Site type" ,
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 90 AND field_id = '130' AND option_id = b_sites.data->>'status'), '') as "Site status",  
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
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 46 AND value_id = b_sites.data->>'power_configuration'), '') as "Power configuration",
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
;

%___________________________________________________________________________
%tenants
%___________________________________________________________________________

table = "tenants"

Select
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
 ((b_tenants.data ->>'entity') IN ('2'))
;

%___________________________________________________________________________
%Teams
%___________________________________________________________________________

table = "teams"

select
  b_teams.data->>'system_name' as "system_name",
  CONCAT('["',b_teams.data->>'system_name','"]') AS "system_name2",
  b_teams.data->>'team_name' as "Team name"
 FROM forms_data as b_teams 
 WHERE b_teams.form_id in (4) AND 
  b_teams.enabled  = true AND 
 ( b_teams.embedded = false OR b_teams.embedded is null)
;

%___________________________________________________________________________
%Users
%___________________________________________________________________________

table = "users"

select
  b_teams.data->>'username' as "system_name",
  CONCAT('["',b_teams.data->>'username','"]') AS "system_name2",
  b_teams.data->>'loginName' as "Login name",
  b_teams.data->>'firstname' as "First name",
  b_teams.data->>'lastname' as "Last name"
 FROM forms_data as b_teams 
 WHERE b_teams.form_id in (1) AND 
  b_teams.enabled  = true AND 
 ( b_teams.embedded = false OR b_teams.embedded is null)
;

%___________________________________________________________________________
#Customer requests
%___________________________________________________________________________

table = "customer requests"

select
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
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 85 AND value_id = b_requests.data->>'cr_activity'), '') as "CR activity",
  b_requests.data->>'application_sow' as "Application SOW",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 28 AND value_id = b_requests.data->>'application_revision'), '') as "Application revision",  
  b_requests.data->>'request_id' as "Space management and Structural"
  FROM forms_data as b_requests
 WHERE b_requests.form_id in (37) AND 
  b_requests.enabled  = true AND 
 ( b_requests.embedded = false OR b_requests.embedded is null)
;

%___________________________________________________________________________
#CR Approval matrix
%___________________________________________________________________________

table = "cr_approval_matrix"

select
  b_approval.data->'request_id' ->>'prefix' as "CAR ID - prefix",
  b_approval.data->'request_id' ->>'number' as "CAR ID - number",
  CONCAT(b_approval.data->'request_id' ->>'prefix', '-',b_approval.data->'request_id' ->>'number') AS "CAR ID",
  b_approval.data->>'approved_by' as "Team",
  b_approval.data->>'team' as "Team1",
  b_approval.data->>'approving' as "Approving",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 22 AND field_id = '2' AND option_id = b_approval.data->>'decision'), '') as "Decision",
  b_approval.data->>'comment' as "Comment",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_approval.data->>'date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Date"
  FROM forms_data as b_approval 
 WHERE b_approval.form_id in (22) AND 
  b_approval.enabled  = true AND 
 ( b_approval.embedded = false OR b_approval.embedded is null)
;

%___________________________________________________________________________
#CR Comments
%___________________________________________________________________________

table = "cos_report_cr_comments"

select  
  CASE WHEN (b_customer_request.data->>'request_id' != '')  THEN (  CASE  WHEN (b_customer_request.data->'request_id'->>'draft' = 'true')  THEN (b_customer_request.data->'request_id'->>'draft_number')  WHEN (b_customer_request.data->'request_id'->>'number' != '')  THEN ( CONCAT(  CASE  WHEN ( b_customer_request.data->'request_id'->>'prefix' != '')  THEN ( b_customer_request.data->'request_id'->>'prefix' )  ELSE '' END  , '-',  CASE  WHEN ( LENGTH(b_customer_request.data->'request_id'->>'number') > 4)  THEN ( b_customer_request.data->'request_id'->>'number')  ELSE ( LPAD(b_customer_request.data->'request_id'->>'number', 4, '0') )  END  ) )  ELSE '' END  ) ELSE '' END  AS "CAR ID" ,
  r_cr_contain_comment_remark.data->>'internal_detail_of_issue' as "Comment",
  CASE WHEN (r_cr_contain_comment_remark.data->>'remark_id' != '')  THEN (  CASE  WHEN (r_cr_contain_comment_remark.data->'remark_id'->>'draft' = 'true')  THEN (r_cr_contain_comment_remark.data->'remark_id'->>'draft_number')  WHEN (r_cr_contain_comment_remark.data->'remark_id'->>'number' != '')  THEN ( CONCAT(  CASE  WHEN ( r_cr_contain_comment_remark.data->'remark_id'->>'prefix' != '')  THEN ( r_cr_contain_comment_remark.data->'remark_id'->>'prefix' )  ELSE '' END  , '-',  CASE  WHEN ( LENGTH(r_cr_contain_comment_remark.data->'remark_id'->>'number') > 4)  THEN ( r_cr_contain_comment_remark.data->'remark_id'->>'number')  ELSE ( LPAD(r_cr_contain_comment_remark.data->'remark_id'->>'number', 4, '0') )  END  ) )  ELSE '' END  ) ELSE '' END  AS "Comment ID" , 
  TO_CHAR(TO_TIMESTAMP(( NULLIF(r_cr_contain_comment_remark.data->>'date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Date",
  (select ((d.data ->> 'firstname'::text) || ' '::text || (d.data ->> 'lastname'::text)) from forms_data d where d.enabled and d.form_id = 1 and d.id = (r_cr_contain_comment_remark.data->>'raised_by')::text) AS "Raised by"
 FROM forms_data as b_customer_request 
 left join forms_relations_data as r0 on r0.relation_id = 67 and (r0.source_id = b_customer_request.id or r0.target_id = b_customer_request.id ) and r0.enabled = true 
 left join forms_data as r_cr_contain_comment_remark on (r_cr_contain_comment_remark.id = r0.source_id or r_cr_contain_comment_remark.id =r0.target_id ) and r_cr_contain_comment_remark.form_id = 80 
 WHERE b_customer_request.form_id in (37) AND b_customer_request.enabled  = true AND ( b_customer_request.embedded = false OR b_customer_request.embedded is null);
;

%___________________________________________________________________________
#Tower structure
%___________________________________________________________________________

table = "tower_structure"

select b_structure.data->>'site_id' as "Site ID",
  b_structure.data->'tower_id' ->>'prefix' as "Tower ID - prefix",
  b_structure.data->'tower_id' ->>'number' as "Tower ID - number",
  CONCAT(b_structure.data->'tower_id' ->>'prefix',TO_CHAR((b_structure.data->'tower_id' ->>'number')::bigint, '0000')::text) as "Tower ID",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 40 AND value_id = b_structure.data->>'location_type'), '') as "Site type",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 68 AND value_id = b_structure.data->>'type_of_structure'), '') as "Structure type",
  b_structure.data->>'structure_type_for_others_only' as "Structure type for others only",
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
;

%___________________________________________________________________________
#Item structural analysis
%___________________________________________________________________________

table = "item_structural_analysis"

select b_itemstructural.data->'analyse_id'->>'number' as "Analysis ID",
  b_itemstructural.data->'item_t_key'->>'number' as "Item key",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 62 AND value_id = b_itemstructural.data->>'item'), '') as "Item",
  b_itemstructural.data->>'value' as "Value"
 FROM forms_data as b_itemstructural
 WHERE b_itemstructural.form_id in (95) AND 
  b_itemstructural.enabled  = true AND 
 ( b_itemstructural.embedded = false OR b_itemstructural.embedded is null)
;

%___________________________________________________________________________
#Item structural analysis
%___________________________________________________________________________

table = "item_foundation_analysis"

select b_itemfoundation.data->'analyse_id'->>'number' as "Analysis ID",
  b_itemfoundation.data->'item_a_key'->>'number' as "Item A key",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 35 AND value_id = b_itemfoundation.data->>'item'), '') as "Item",
  b_itemfoundation.data->>'value' as "Value"
 FROM forms_data as b_itemfoundation
 WHERE b_itemfoundation.form_id in (56) AND 
  b_itemfoundation.enabled  = true AND 
 ( b_itemfoundation.embedded = false OR b_itemfoundation.embedded is null)
;

%___________________________________________________________________________
#Analysis
%___________________________________________________________________________

table = "analysis"


select b_analysis.data->>'site_id' as "Site ID",
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
;


%___________________________________________________________________________
#O&M actions
%___________________________________________________________________________

table = "o_m_actions"

select 
  b_actions.data->'action_id' ->>'prefix' as "Action ID - prefix",
  b_actions.data->'action_id' ->>'number' as "Action ID  - number",
  b_actions.data->'action_id' ->>'number' as "Action ID",
  b_actions.data->>'anchor_id' as "Anchor ID",
  b_actions.data->>'site_id_text' as "Site ID",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 32 AND value_id = b_actions.data->>'entity'), '') as "Entity",
  b_actions.data->>'zone_team' as "Zone",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 63 AND value_id = b_actions.data->>'anchor_class'), '') as "Anchor class",
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 46 AND value_id = b_actions.data->>'power_configuration'), '') as "Power configuration",
  b_actions.data->>'week' as "Week",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_actions.data->>'date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Open date",
  b_actions.data->>'week_raw_sla' as "Week raw SLA",
  b_actions.data->>'repetitive_outages' as "Repetitive outages",
  b_actions.data->>'most_frequent_rca' as "RCA",
  b_actions.data->>'rca_sub_category' as "RCA sub category",
  b_actions.data->>'rca_summary' as "RCA summary",
  b_actions.data->>'action_plan' as "Action plan",
  b_actions.data->>'action_by' as "Action by",
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_actions.data->>'action_due','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Action due",
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 120 AND field_id = '13' AND option_id = b_actions.data->>'status'), '') as "Status",
  b_actions.data->>'created_by' as "Created by"
 FROM forms_data as b_actions
 WHERE b_actions.form_id in (120) AND 
  b_actions.enabled  = true AND 
 ( b_actions.embedded = false OR b_actions.embedded is null)
;


%___________________________________________________________________________
#Community issues
%___________________________________________________________________________

table = "community_issues"

select
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
;


%___________________________________________________________________________
#Comments
%___________________________________________________________________________

table = "comments"

select
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
;

%___________________________________________________________________________
#Restrictions
%___________________________________________________________________________

table = "restrictions"

select
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
;
