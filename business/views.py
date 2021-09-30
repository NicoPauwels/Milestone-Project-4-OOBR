from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings

# from business.models import Business, User
# from business.forms import BusinessForm

from formtools.wizard.views import CookieWizardView

# Create your views here.

class BusinessConfigWizard(CookieWizardView):

    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'media'))

    def get_template_names(self):
        return ['business/configure_business.html']


    """
    def done(self, form_list, **kwargs):
        return render(self.request, 'add_business.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
    """

    """
    def add_business(request):
        if request.method == "POST":
            form = BusinessForm(data=request.POST)
            user = get_object_or_404(User, email=request.user)
            if form.is_valid():
                data = form.cleaned_data
                business = Business.objects.create(
                    user = user,
                    name = data['name'],
                    image = data['image'],
                    owner_firstname = data['owner_firstname'],
                    owner_lastname = data['owner_lastname'],
                    address_1 = data['address_1'],
                    address_2 = data['address_2'],
                    postal_code = data['postal_code'],
                    city = data['city'],
                    contact_number = data['contact_number'],
                    VAT_number = data['VAT_number'],
                    bankaccount_number = data['bankaccount_number'],
                )
                business.save()
                return HttpResponseRedirect('/success/')
        else:
            form = BusinessForm()

        template = 'business/add_business.html'
        context = { 
                    'form': form
                }

        return render(request, template, context)
    """
    """ Add business details 
        user = get_object_or_404(User, email=request.user)
        print(user)

        form = BusinessForm()
        template = 'business/add_business.html'
        context = {
            'form': form,
        }

        return render(request, template, context)
        """
