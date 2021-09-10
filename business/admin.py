from django.contrib import admin
from business.models import BusinessDetails

# Register your models here.
class BusinessDetailsAdmin(admin.ModelAdmin):

    list_display = ('user', 'business_owner', 'contact_number', 'VAT_number', 'bankaccount_number')

admin.site.register(BusinessDetails, BusinessDetailsAdmin)