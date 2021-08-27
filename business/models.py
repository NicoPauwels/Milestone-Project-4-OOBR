from django.db import models


class Business(models.Model):
    class Meta:
        verbose_name_plural = 'Businesses'

    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name