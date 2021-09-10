from user.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser

class BusinessUserSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'email', 'password1', 'password2', 'business_name'
        ]

    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.business_name = self.cleaned_data['business_name']
        user.is_company_user = True
        user.save()