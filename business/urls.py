from django.urls import path
from . import views

urlpatterns = [
    path('add_business/', views.add_business, name='add_business'),
]