from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username','email','full_name','role','is_active','date_joined')
    list_filter = ('role','is_active')
    search_fields = ('username','email','full_name')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('username','email','password')}),
        ('Personal', {'fields': ('full_name','address','contact_number','gender','age_range')}),
        ('Permissions', {'fields': ('role','is_active','is_staff','is_superuser')}),
    )
    add_fieldsets = ((None, {'classes':('wide',),'fields':('username','email','password1','password2','role')}),)
