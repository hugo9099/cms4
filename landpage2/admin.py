from django.contrib import admin

from . import models


@admin.register(models.Campaign)
class CampaignAdmin(admin.ModelAdmin):
    ordering = ('id',)
    fieldsets = [
        ('Basic Information', {
            'fields': [('name', 'lead_type'), 'creation_date', 'LP_version', 'phone_number', ('default_src',
                       'default_affref') ]}),
        ('Phone Number Showing', {
            'fields': ['index_phone_header', 'index_phone_footer', 'form_phone_header', 'form_phone_footer',
                       'thankyou_phone_header', 'thankyou_phone_footer', ],
            'classes': ['collapse']}),
        ('Questions to Include on Form', {
            'fields': ['self_emp', 'insured', 'spouse', 'no_of_children', 'est_income', 'affordable', 'hospitalized',
                       'physician', 'prescription', 'previously_denied', 'ss_disabled', 'pregnant', 'health',
                       'household_size', 'expected_income', 'click_agree_terms_cond', 'affil_contact', ],
            'classes': ['collapse']})
    ]
    list_display = ['id', 'name', 'LP_version', 'lead_type', 'phone_number', 'description', 'creation_date']
    list_display_links = ('id', 'name')
    list_filter = ['lead_type', 'LP_version']
    search_fields = ['name']


@admin.register(models.LeadType)
class LeadTypeAdmin(admin.ModelAdmin):
    ordering = ('type',)
    list_display = ('type', 'name', 'specs')


@admin.register(models.LandPageVersion)
class LPVersionAdmin(admin.ModelAdmin):
    ordering = ('lpver',)
    list_display = ('lpver', 'name', 'creation_date')

