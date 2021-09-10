from django.db.models.deletion import CASCADE
from user.models import CustomUser
from django.db import models


class BusinessDetails(models.Model):
    class Meta:
        verbose_name_plural = 'Businesses'

    user = models.ForeignKey(CustomUser, on_delete=CASCADE, default='')
    business_owner = models.CharField(max_length=80, blank=False, default='')
    contact_number = models.CharField(max_length=80, blank=False, default='')
    VAT_number = models.CharField(max_length=80, blank=False, default='')
    bankaccount_number = models.CharField(max_length=80, blank=False, default='')
    
    def __str__(self):
        return self.business_owner