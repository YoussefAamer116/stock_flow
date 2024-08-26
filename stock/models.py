from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.item_name
