from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    is_business_user = models.BooleanField(default=False)
    is_customer_user = models.BooleanField(default=False)

class BusinessUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    business_name = models.CharField(max_length=150, blank=False)