from django.db import models
from stock.models import Item

# Create your models here.

class Sale(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Ensure that the quantity sold is positive
        if self.quantity_sold <= 0:
            raise ValueError('Quantity sold must be positive.')

        # Update stock quantity
        if self.item.quantity < self.quantity_sold:
            raise ValueError('Not enough stock to sell the requested quantity.')
        
        self.item.quantity -= self.quantity_sold
        self.item.save()
        self.total_revenue = self.quantity_sold * self.item.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity_sold} of {self.item.item_name} on {self.sale_date}"