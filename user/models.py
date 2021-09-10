from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    username = models.CharField(max_length=40, unique=True, default='')
    email = models.EmailField(max_length=254, unique=True, default='')
    is_company_user = models.BooleanField(default=False)
    is_customer_user = models.BooleanField(default=False)
    business_name = models.CharField(max_length=80, blank = False, default = '')

    def __str__(self):
        return self.username
    
