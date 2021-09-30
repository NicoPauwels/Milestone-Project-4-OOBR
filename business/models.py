from django.db import models
from django.db.models.fields.files import ImageField
from users.models import User


class BusinessType(models.Model):

    business_type = models.CharField(max_length=48, verbose_name='Business Type', blank=False)

    class Meta:
        ordering = ('business_type',)

    def __str__(self):
        return self.business_type

class BusinessCategory(models.Model):

    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE, verbose_name='Business Type')
    business_category = models.CharField(max_length=48, verbose_name='Business Category', unique=True)

    class Meta:
        verbose_name_plural = "Business categories"
        ordering = ('business_type', 'business_category',)

    def __str__(self):
        return self.business_category


class MenuCategory(models.Model):

    menu_category = models.CharField(max_length=48, verbose_name='Menu Category', blank=False)

    class Meta:
        ordering = ('menu_category',)

    def __str__(self):
        return self.menu_category


class MenuSubCategory(models.Model):

    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, verbose_name='Menu Category Name')
    menu_subcategory = models.CharField(max_length=48, verbose_name='Menu Subcategory', blank=False)

    class Meta:
        ordering = ('menu_category', 'menu_subcategory',)

    def __str__(self):
        return self.menu_subcategory


class Business(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # Business Heading

    display_name = models.CharField(max_length=254, blank=False, default='Display Name')
    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE, blank=False)
    business_category = models.ForeignKey(BusinessCategory, on_delete=models.CASCADE, blank=False)
    banner_image = ImageField(blank=False, null=True, unique=True)

    # Business Details

    business_name = models.CharField(max_length=254, blank=False, default='Business Name')
    contact_firstname = models.CharField(max_length=254, blank=False, default='Contact First Name')
    contact_lastname = models.CharField(max_length=254, blank=False, default='Contact First Name')
    address_1 = models.CharField(max_length=254, blank=False, default='Address 1')
    address_2 = models.CharField(max_length=254, blank=True, default='Address 2')
    postal_code = models.CharField(max_length=6, blank=False,default='Postal Code')
    city = models.CharField(max_length=254, blank=False, default='City')
    contact_number = models.CharField(max_length=15, blank=False, default='Contact Number')
    VAT_number = models.CharField(max_length=12, blank=False, default='VAT Number')
    bankaccount_number = models.CharField(max_length=16, blank=False, default='Bank Account Number')

    class Meta:
        verbose_name_plural = 'Businesses'

    def __str__(self):
        return self.name