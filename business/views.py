from user.models import CustomUser
from django.shortcuts import redirect
from django.views.generic import CreateView

from business.models import BusinessDetails
from business.forms import BusinessDetailsForm

# Create your views here.

class BusinessDetailsView(CreateView):
    model = BusinessDetails
    form_class = BusinessDetailsForm
    template_name = 'business/business_details.html'

    def form_valid(self, form):
        business_details = form.save(commit=False)
        business_details.user = self.request.user
        business_details.save()
        return redirect('business_locations')


# def business_details(request):
#    form = BusinessDetailForm()
#    template = 'business/business_details.html'
#    context = {
#        'form': form,
#    }

#    return render(request, template, context)