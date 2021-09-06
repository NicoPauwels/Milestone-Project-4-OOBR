from django.db.models.base import Model
from django.forms import ModelForm
from user.models import BusinessUser

class BusinessUserSignUpForm(ModelForm):
    class Meta:
        model = BusinessUser
        fields = ['user','business_name']