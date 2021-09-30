from business.forms import BusinessDetail, BusinessHeading, BusinessMenu, BusinessMenuItems, BusinessTables
from django.urls import path
from business.views import BusinessConfigWizard
from business.forms import BusinessHeading, BusinessDetail, BusinessTables, BusinessMenu, BusinessMenuItems

urlpatterns = [
    path('configure/', BusinessConfigWizard.as_view([BusinessHeading, BusinessDetail, BusinessTables, BusinessMenu, BusinessMenuItems]), name='configure_business'),
]