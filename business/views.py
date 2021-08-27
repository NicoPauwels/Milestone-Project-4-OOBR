from business.forms import BusinessForm
from django.shortcuts import render

from .forms import BusinessForm

# Create your views here.

def add_business(request):
    """ Register """
    form = BusinessForm()
    template = 'business/add_business.html'
    context = {
        'form': form,
    }

    return render(request, template, context)