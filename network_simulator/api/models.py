from django.db import models

# Create your models here.
from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.name
