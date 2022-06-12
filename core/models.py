from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.name
