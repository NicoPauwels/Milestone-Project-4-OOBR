from django.shortcuts import render

from business.forms import BusinessForm

# Create your views here.

def add_business(request):
    """ Add a business """
    form = BusinessForm()
    template = 'business/add_business.html'
    context = {
        'form': form,
    }

    return render(request, template, context)