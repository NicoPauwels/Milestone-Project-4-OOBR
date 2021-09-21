from django.contrib import admin
from business.models import Business

# Register your models here.

class BusinessAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'owner_firstname',
        'owner_lastname', 
        'address_1',
        'address_2 ',
        'postal_code',
        'city', 
        'contact_number',
        'VAT_number',
        'bankaccount_number',
        'rating',
    )

    ordering = (
        'name',
    )

admin.site.register(Business, BusinessAdmin)