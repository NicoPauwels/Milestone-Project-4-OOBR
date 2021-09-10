from django.contrib import admin
from user.models import CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'business_name', 'is_company_user', 'is_customer_user')

admin.site.register(CustomUser, CustomUserAdmin)