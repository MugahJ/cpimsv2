from django.conf.urls import patterns, url

# This should contain urls related to registry ONLY
urlpatterns = patterns(
    # Forms Registry
    'cpovc_forms.views',
    url(r'^$', 'forms_home', name='forms'),
    url(r'^forms_registry/$', 'forms_registry',
        name='forms_registry'),

    # Documents Manager
    url(r'^documents_manager/$', 'documents_manager',
        name='documents_manager'),
    url(r'^documents_manager_search/$', 'documents_manager_search',
        name='documents_manager_search'),

    # Case Record Sheet Urls
    url(r'^case_record_sheet/$', 'case_record_sheet',
        name='case_record_sheet'),
    url(r'^new_case_record_sheet/(?P<id>\d+)/$', 'new_case_record_sheet',
        name='new_case_record_sheet'),
    url(r'^view_case_record_sheet/(?P<id>\w+)/$', 'view_case_record_sheet',
        name='view_case_record_sheet'),
    url(r'^edit_case_record_sheet/(?P<id>\w+)/$', 'edit_case_record_sheet',
        name='edit_case_record_sheet'),
    url(r'^delete_case_record_sheet/(?P<id>\w+)/$', 'delete_case_record_sheet',
        name='delete_case_record_sheet'),

    # Alternative Family Care Urls
    url(r'^alternative_family_care/$', 'alternative_family_care',
        name='alternative_family_care'),
    url(r'^new_alternative_family_care/(?P<id>\d+)/$', 'new_alternative_family_care',
        name='new_alternative_family_care'),
    url(r'^edit_alternative_family_care/(?P<id>\w+)/$', 'edit_alternative_family_care',
        name='edit_alternative_family_care'),
    url(r'^view_alternative_family_care/(?P<id>\w+)/$', 'view_alternative_family_care',
        name='view_alternative_family_care'),

    # Residential Placement
    url(r'^save_placement/$', 'save_placement',
        name='save_placement'),
    url(r'^view_placement/(?P<id>\w+)/$', 'view_placement',
        name='view_placement'),
    url(r'^edit_placement/(?P<id>\w+)/$', 'edit_placement',
        name='edit_placement'),
    url(r'^delete_placement/$', 'delete_placement',
        name='delete_placement'),
    url(r'^residential_placement/$',
        'residential_placement', name='residential_placement'),
    url(r'^placement/(?P<id>\d+)/$',
        'placement', name='placement'),

    # Residential Placement FollowUp
    url(r'^placement_followup/(?P<id>\d+)/$',
        'placement_followup', name='placement_followup'),
    url(r'^save_placementfollowup/$',
        'save_placementfollowup', name='save_placementfollowup'),
    url(r'^view_placementfollowup/$',
        'view_placementfollowup', name='view_placementfollowup'),
    url(r'^edit_placementfollowup/$', 'edit_placementfollowup',
        name='edit_placementfollowup'),
    url(r'^delete_placementfollowup/$', 'delete_placementfollowup',
        name='delete_placementfollowup'),

    # Case Events (Encounters/Court Sessions/Referrals/Case
    # Closure/Summons)
    url(r'^case_events/(?P<id>\w+)/$', 'case_events',
        name='case_events'),
    # ---------------------------------------------------------
    url(r'^save_encounter/$', 'save_encounter',
        name='save_encounter'),
    url(r'^view_encounter/$', 'view_encounter',
        name='view_encounter'),
    url(r'^edit_encounter/$', 'edit_encounter',
        name='edit_encounter'),
    url(r'^delete_encounter/$', 'delete_encounter',
        name='delete_encounter'),
    # ----------------------------------------------------------
    url(r'^save_court/$', 'save_court', name='save_court'),
    url(r'^view_court/$', 'view_court',
        name='view_court'),
    url(r'^edit_court/$', 'edit_court',
        name='edit_court'),
    url(r'^delete_court/$', 'delete_court',
        name='delete_court'),
    #------------------------------------------------------------
    url(r'^save_summon/$', 'save_summon', name='save_summon'),
    url(r'^edit_summon/$', 'edit_summon', name='edit_summon'),
    url(r'^view_summon/$', 'view_summon', name='view_summon'),
    url(r'^delete_summon/$', 'delete_summon',
        name='delete_summon'),
    #------------------------------------------------------------    
    url(r'^save_closure/$', 'save_closure', name='save_closure'),
    url(r'^edit_closure/$', 'edit_closure', name='edit_closure'),
    url(r'^view_closure/$', 'view_closure', name='view_closure'),
    url(r'^delete_closure/$', 'delete_closure', name='delete_closure'),

    # Referrals
    url(r'^delete_referral/$', 'delete_referral',
        name='delete_referral'),

    # Management Urls
    url(r'^manage_refferal/$', 'manage_refferal',
        name='manage_refferal'),
    url(r'^manage_refferal001/$', 'manage_refferal001',
        name='manage_refferal001'),
    url(r'^manage_refferal002/$', 'manage_refferal002',
        name='manage_refferal002'),
    url(r'^manage_refferal003/$', 'manage_refferal003',
        name='manage_refferal003'),
    url(r'^manage_casecategory001/$', 'manage_casecategory001',
        name='manage_casecategory001'),
    url(r'^manage_casecategory002/$', 'manage_casecategory002',
        name='manage_casecategory002'),
    url(r'^manage_casecategory003/$', 'manage_casecategory003',
        name='manage_casecategory003'),
    url(r'^manage_casecategory004/$', 'manage_casecategory004',
        name='manage_casecategory004'),
    url(r'^manage_encounters001/$', 'manage_encounters001',
        name='manage_encounters001'),
    url(r'^manage_encounters004/$', 'manage_encounters004',
        name='manage_encounters004'),
    url(r'^manage_case_events/$', 'manage_case_events',
        name='manage_case_events'),
    url(r'^manage_placementfollowup/$', 'manage_placementfollowup',
        name='manage_placementfollowup'),
    url(r'^manage_schools/$', 'manage_schools',
        name='manage_schools'),
    url(r'^manage_countries/$', 'manage_countries',
        name='manage_countries'),
    url(r'^manage_casehistory/$', 'manage_casehistory',
        name='manage_casehistory'),
    url(r'^manage_service_category/$', 'manage_service_category',
        name='manage_service_category'),
    url(r'^manage_form_type/$', 'manage_form_type',
        name='manage_form_type'),
    # ---------------------------------------------------------------
    url(r'^userorgunits_lookup/$', 'userorgunits_lookup',
        name='userorgunits_lookup'),
    url(r'^usersubcounty_lookup/$', 'usersubcounty_lookup',
        name='usersubcounty_lookup'),
    url(r'^userward_lookup/$', 'userward_lookup',
        name='userward_lookup'),
    url(r'^generate_serialnumber/$', 'generate_serialnumber',
        name='generate_serialnumber'),
    url(r'^getJsonObject001/$', 'getJsonObject001',
        name='getJsonObject001'),

    # Search Urls
    url(r'^ovc_search/$', 'ovc_search', name='ovc_search'),

    # School & Bursary Urls
    url(r'^background_details/$', 'background_details',
        name='background_details'),
    url(r'^new_education_info/(?P<id>\d+)/$',
        'new_education_info', name='new_education_info'),
    url(r'^edit_education_info/(?P<id>\w+)/$',
    'edit_education_info', name='edit_education_info'),
    url(r'^view_education_info/(?P<id>\w+)/$',
        'view_education_info', name='view_education_info'),
    url(r'^delete_education_info/(?P<id>\w+)/$',
        'delete_education_info', name='delete_education_info'),
    # -----------------------------------------------------------------
    url(r'^new_school/$',
        'new_school', name='new_school'),
    # ------------------------------------------------------------------
    url(r'^new_bursary_info/$',
        'new_bursary_info', name='new_bursary_info'),
    url(r'^edit_bursary_info/$',
    'edit_bursary_info', name='edit_bursary_info'),
    url(r'^view_bursary_info/$',
    'view_bursary_info', name='view_bursary_info'),
    url(r'^delete_bursary_info/$',
    'delete_bursary_info', name='delete_bursary_info'),
    url(r'^bursary_followup/(?P<id>\d+)/$',
        'bursary_followup', name='bursary_followup'),
    url(r'^manage_bursary/$',
        'manage_bursary', name='manage_bursary'),
    
    # OVC Care
    url(r'^csi/$',
        'csi', name='csi'),
    url(r'^new_csi/(?P<id>\d+)/$',
        'new_csi', name='new_csi'),
    url(r'^edit_csi/(?P<id>\w+)/$',
        'edit_csi', name='edit_csi'),
    url(r'^view_csi/(?P<id>\w+)/$',
        'view_csi', name='view_csi'),
    url(r'^delete_csi/(?P<id>\w+)/$',
        'delete_csi', name='delete_csi'),

    url(r'^form1a_events/(?P<id>\d+)/$',
        'form1a_events', name='form1a_events'),
    url(r'^save_form1a/$',
        'save_form1a', name='save_form1a'),
    url(r'^edit_form1a/$',
        'edit_form1a', name='edit_form1a'),
    url(r'^view_form1a/$',
        'view_form1a', name='view_form1a'),
    url(r'^delete_form1a/$',
        'delete_form1a', name='delete_form1a'),   
    url(r'^manage_form1a_events/$',
        'manage_form1a_events', name='manage_form1a_events'),

    url(r'^new_hhva/(?P<id>\d+)/$',
        'new_hhva', name='new_hhva'),
    url(r'^edit_hhva/(?P<id>\w+)/$',
        'edit_hhva', name='edit_hhva'),
    url(r'^view_hhva/(?P<id>\w+)/$',
        'view_hhva', name='view_hhva'),
    url(r'^delete_hhva/(?P<id>\w+)/$',
        'delete_hhva', name='delete_hhva'),

)
