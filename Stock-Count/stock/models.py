from django.db import models


class Stock(models.Model):
    foodName = models.CharField(max_length = 200, verbose_name="Product")
    quantity = models.IntegerField(blank=True, null=True)
    dateTime = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.foodName


    # one stock-id can have many transactions records
class Transaction(models.Model):

     quantity = models.IntegerField(blank=True, null=True)
     timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=True)
     stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

     def __str__(self):
        return self.stock.foodName