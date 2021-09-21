from django import forms
from business.models import Business

class BusinessForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = ['name', 'image', 'owner_firstname', 'owner_lastname', 'address_1', 'address_2', 'postal_code', 'city', 'contact_number', 'VAT_number', 'bankaccount_number']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            for field in self.fields.items():
                field.widget.attrs['class'] = 'border-black rounded-0'