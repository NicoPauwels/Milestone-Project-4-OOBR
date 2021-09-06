from django.urls import path
from user.views import SignUpBusinessUserView

urlpatterns = [
    path('signup_business/', SignUpBusinessUserView.as_view(), name='signup-business')
]