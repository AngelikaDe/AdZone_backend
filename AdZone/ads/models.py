from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    photo_link1 = models.URLField(blank=True)
    photo_link2 = models.URLField(blank=True)
    photo_link3 = models.URLField(blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)

def __str__(self):
        return self.name
