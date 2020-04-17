from django.db import models

class Stock(models.Model):
    foodName = models.CharField(max_length = 200)
    quantity = models.IntegerField()
    outOfStock = models.BooleanField(None)

    def __str__(self):
        return self.foodName