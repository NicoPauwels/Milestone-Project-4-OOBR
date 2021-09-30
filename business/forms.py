from django import forms
from django.forms import ModelForm
from django.db.models import F, fields
from django.db.models.fields.files import ImageField
from django.forms.widgets import Select
from business.models import BusinessType, BusinessCategory, MenuCategory, MenuSubCategory, Business


class BusinessHeading(ModelForm):

    business_type = forms.ModelChoiceField(
        queryset=BusinessType.objects.all(),
        empty_label="Select Type"
    )

    business_category = forms.ModelChoiceField(
        queryset=BusinessCategory.objects.all(),
        empty_label="Select Category"
    )

    class Meta:
        model = Business
        fields = ['display_name', 'business_type', 'business_category', 'banner_image']

    
class BusinessDetail(forms.Form):

    business_name = forms.CharField(max_length=100)
    contact_person = forms.CharField(max_length=100)
    address_1 = forms.CharField(max_length=100)
    address_2 = forms.CharField(max_length=100)
    postal_code = forms.CharField(max_length=6)
    city = forms.CharField(max_length=100)
    telephone_number = forms.CharField(max_length=20)
    VAT_number = forms.CharField(max_length=20)
    bankaccount_number = forms.CharField(max_length=20)


class BusinessTables(forms.Form):

    number_of_tables = forms.IntegerField(min_value=1, max_value=200)


class BusinessMenu(forms.Form):
        
    menu_name = forms.CharField(max_length=100)


class BusinessMenuItems(forms.Form):

    menu_category = forms.ModelChoiceField(
        queryset=MenuCategory.objects.all(),
        widget=forms.Select()
        )

    menu_subcategory = forms.ModelChoiceField(
        queryset=MenuSubCategory.objects.values('menu_category_id'),
        widget=forms.Select(),
    )

    item = forms.CharField(max_length=100)
    item_description = forms.CharField(max_length=254)
    price = forms.DecimalField(min_value=0, max_value=1000, max_digits=5, decimal_places=2)


"""
class BusinessForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = ['name', 'image', 'owner_firstname', 'owner_lastname', 'address_1', 'address_2', 'postal_code', 'city', 'contact_number', 'VAT_number', 'bankaccount_number']

        
        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(BusinessForm, self).__init__(*args, **kwargs)
            
            for field in self.fields.items():
                field.widget.attrs['class'] = 'border-black rounded-0'
"""        