from user.forms import BusinessUserSignUpForm
from user.models import BusinessUser
from django.views.generic.edit import CreateView

class SignUpBusinessUserView(CreateView):
    model = BusinessUser
    form_class = BusinessUserSignUpForm
    template = 'signup_business.html'

