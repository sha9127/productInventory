from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=125)
    category=models.CharField(max_length=125)
    price = models.FloatField()

    def __str__(self) -> str:
        return '{}-{}'.format(self.name, self.category)