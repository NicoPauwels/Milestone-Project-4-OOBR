from django.urls import path
from user.views import BusinessUserSignUpView

urlpatterns = [
    path('signup_business/', BusinessUserSignUpView.as_view(), name='signup-business')
]