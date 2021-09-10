from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from user.models import CustomUser
from user.forms import BusinessUserSignUpForm

class BusinessUserSignUpView(CreateView):
    model = CustomUser
    form_class = BusinessUserSignUpForm
    template_name = 'signup_business.html'

    #def get_context_data(self, **kwargs):
    #    kwargs['user_type'] = 'business'
    #    return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('business_details')

    