from django.db import models
from django.db.models.fields.files import ImageField
from users.models import User


class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=254, blank=False)
    image = ImageField(null=True, blank=True)
    owner_firstname = models.CharField(max_length=254, blank=False)
    owner_lastname = models.CharField(max_length=254, blank=False)
    address_1 = models.CharField(max_length=254, blank=False)
    address_2 = models.CharField(max_length=254, blank=True)
    postal_code = models.CharField(max_length=4, blank=False)
    city = models.CharField(max_length=254, blank=False)
    contact_number = models.CharField(max_length=15, blank=False)
    VAT_number = models.CharField(max_length=12, blank=False)
    bankaccount_number = models.CharField(max_length=16, blank=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=False)

    def __str__(self):
        return self.name


