from django.urls import path
from business import views

urlpatterns = [
    path('add/', views.add_business, name='add_business')
]