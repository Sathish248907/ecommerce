from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display  = ('company_id', 'name', 'contact_number', 'is_active')
    search_fields = ('company_id', 'name')
    ordering      = ('name',)
