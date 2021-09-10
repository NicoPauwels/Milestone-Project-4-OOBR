from django import forms
from business.models import BusinessDetails


class BusinessDetailsForm(forms.ModelForm):

    class Meta:
        model = BusinessDetails  
        fields = [
            'business_owner', 'contact_number', 'VAT_number', 'bankaccount_number'
        ]
