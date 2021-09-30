from django.shortcuts import render
from allauth.account.views import SignupView
from users.forms import BusinessUserSignupForm

# Create your views here.

class BusinessUserSignupView(SignupView):
    
    template_name = 'allauth/account/signupbusiness.html'
    form_class = BusinessUserSignupForm
    redirect_field_name = 'next'
    view_name = 'signupbusiness'
    
    def get_context_data(self, **kwargs):
        ret = super(BusinessUserSignupView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret
        
signupbusiness = BusinessUserSignupView.as_view()
 

