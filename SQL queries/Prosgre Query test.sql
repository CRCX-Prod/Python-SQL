**Original**

Select b_sites.id AS id,  b_sites.data->>'site_id_text' as "Site ID" ,
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 104 AND value_id = b_sites.data->>'entity'), '') as "Entity" , 
  b_sites.data->>'zone_team' as "Zone" , 
  
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_sites.data->>'site_built','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Site Built" ,
      
  TO_CHAR(TO_TIMESTAMP(( NULLIF(r_tenant_contain_location_tenant.data->>'rfi_date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "RFI" ,
  
  TO_CHAR(TO_TIMESTAMP(( NULLIF(r_tenant_contain_location_tenant.data->>'on_air_date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "On air" ,
  
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 113 AND value_id = r_tenant_contain_location_tenant.data->>'power_type'), '') as "Billable power" ,
  COALESCE((SELECT option_title FROM cos_mview_dropdown_radio_values WHERE form_id = 200 AND field_id = '26' AND option_id = r_tenant_contain_location_tenant.data->>'tenant_configuration'), '') as "Tenant configuration" ,
  r_tenant_contain_location_tenant.data->>'tenant_site_id' as "Tenant ID" ,
  
  TO_CHAR(TO_TIMESTAMP(( NULLIF(r_tenant_link_to_lease_site_lease.data->>'boa_date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "BOA" ,
  
  TO_CHAR(TO_TIMESTAMP(( NULLIF(r_tenant_link_to_lease_site_lease.data->>'eoa_date','') )::bigint/1000) , 'YYYY-MM-DD')::text as "EOA" ,
  
  TO_CHAR(TO_TIMESTAMP(( NULLIF(r_tenant_link_to_lease_site_lease.data->>'cut_over','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Cut Over" ,
  
  r_tenant_link_to_lease_site_lease.data->>'tower' as "Tower" ,
  r_tenant_link_to_lease_site_lease.data->>'power' as "Power" ,
  
 TO_CHAR(TO_TIMESTAMP(( NULLIF(r_tenant_link_to_lease_site_lease.data->>'termination_notice','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Termination notice"  
 FROM forms_data as b_sites
 left join forms_relations_data as r0 on r0.relation_id = 1075 and (r0.source_id = b_sites.id or r0.target_id = b_sites.id ) and r0.enabled = true 
 left join forms_data as r_tenant_contain_location_tenant on (r_tenant_contain_location_tenant.id = r0.source_id or r_tenant_contain_location_tenant.id =r0.target_id ) and r_tenant_contain_location_tenant.form_id = 200 
 left join forms_relations_data as r1 on r1.relation_id = 1077 and (r1.source_id = r_tenant_contain_location_tenant.id or r1.target_id = r_tenant_contain_location_tenant.id ) and r1.enabled = true 
 left join forms_data as r_tenant_link_to_lease_site_lease on (r_tenant_link_to_lease_site_lease.id = r1.source_id or r_tenant_link_to_lease_site_lease.id =r1.target_id ) and r_tenant_link_to_lease_site_lease.form_id = 190 
 WHERE b_sites.form_id in (14) AND b_sites.enabled  = true AND ( b_sites.embedded = false OR b_sites.embedded is null)  
;



Test Site only


Select b_sites.id AS id,  b_sites.data->>'site_id_text' as "Site ID" ,
  COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 104 AND value_id = b_sites.data->>'entity'), '') as "Entity" , 
  b_sites.data->>'zone_team' as "Zone" , 
  
  TO_CHAR(TO_TIMESTAMP(( NULLIF(b_sites.data->>'site_built','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Site Built" ,
         
 FROM forms_data as b_sites
 left join forms_relations_data as r0 on r0.relation_id = 1075 and (r0.source_id = b_sites.id or r0.target_id = b_sites.id ) and r0.enabled = true 
 left join forms_data as r_tenant_contain_location_tenant on (r_tenant_contain_location_tenant.id = r0.source_id or r_tenant_contain_location_tenant.id =r0.target_id ) and r_tenant_contain_location_tenant.form_id = 200 
 left join forms_relations_data as r1 on r1.relation_id = 1077 and (r1.source_id = r_tenant_contain_location_tenant.id or r1.target_id = r_tenant_contain_location_tenant.id ) and r1.enabled = true 
 left join forms_data as r_tenant_link_to_lease_site_lease on (r_tenant_link_to_lease_site_lease.id = r1.source_id or r_tenant_link_to_lease_site_lease.id =r1.target_id ) and r_tenant_link_to_lease_site_lease.form_id = 190 
 WHERE b_sites.form_id in (14) AND b_sites.enabled  = true AND ( b_sites.embedded = false OR b_sites.embedded is null)  
;


Sites query working

Select b_sites.id AS id,  b_sites.data->>'site_id_text' as "Site ID" ,  
    COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 104 AND value_id = b_sites.data->>'entity'), '') as "Entity" ,
    TO_CHAR(TO_TIMESTAMP(( NULLIF(b_sites.data->>'site_built','') )::bigint/1000) , 'YYYY-MM-DD')::text as "Site ready date" 

 FROM forms_data as b_sites 
 WHERE b_sites.form_id in (14) AND 
  b_sites.enabled  = true AND 
 ( b_sites.embedded = false OR b_sites.embedded is null) AND 
 ((b_sites.data ->>'entity') IN ('2'))


%Sites

Select
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

%tenants

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


%Field_data



%Test Query for Python

Select b_sites.data->>'site_id_text' as "Site ID" ,  
 COALESCE((SELECT value_title FROM cos_mview_terminology_values WHERE id = 32 AND value_id = b_sites.data->>'entity'), '') as "Entity"
 FROM forms_data as b_sites 
 WHERE b_sites.form_id in (97) AND 
  b_sites.enabled  = true AND 
 ( b_sites.embedded = false OR b_sites.embedded is null) AND 
 ((b_sites.data ->>'site_id_text') IN ('1-01-17006-005'))
 