from django.contrib import admin
from django.db import models

# Register your models here.
from companydata.models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','business_id', 'company_form', 'business_line', 'registration_date', 'city',)
    search_fields = ['name','business_id', 'registration_date', 'city' ]
    list_filter = ('city', 'company_form',)

admin.site.register(Company, CompanyAdmin)