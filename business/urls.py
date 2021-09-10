from django.urls import path
from business.views import BusinessDetailsView

urlpatterns = [
    path('business_details/', BusinessDetailsView.as_view(), name='business_details'),
]