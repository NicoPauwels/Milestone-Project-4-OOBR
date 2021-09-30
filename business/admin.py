from django.contrib import admin
from business.models import Business, BusinessType, BusinessCategory

# Register your models here.

class BusinessAdmin(admin.ModelAdmin):
    
    list_display = (
        'display_name',
        'business_type',
        'business_category',
        'banner_image',
        'business_name', 
        'contact_firstname', 
        'contact_lastname',
        'address_1', 
        'address_2', 
        'postal_code', 
        'city', 
        'contact_number', 
        'VAT_number', 
        'bankaccount_number',
    )

    ordering = (
        'business_name',
    )

admin.site.register(Business, BusinessAdmin)


class BusinessTypeAdmin(admin.ModelAdmin):
   
   list_display = (
        'business_type',
    )

admin.site.register(BusinessType, BusinessTypeAdmin)


class BusinessCategoryAdmin(admin.ModelAdmin):
    
    list_display = (
        'business_type',
        'business_category',
    )

    ordering = (
        'business_type',
        'business_category',
    )

admin.site.register(BusinessCategory, BusinessCategoryAdmin)