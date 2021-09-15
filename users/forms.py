from allauth.account.forms import SignupForm


class BusinessUserSignupForm(SignupForm):

    def save(self, request, commit=True):
        user = super(BusinessUserSignupForm, self).save(request)    
        user.is_business_user = True
        user.save()
        return user