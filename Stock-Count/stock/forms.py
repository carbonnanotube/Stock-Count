from django import forms
from stock.models import Stock, Transaction


class StockForm(forms.ModelForm):  
    class Meta:
        model = Stock
        fields = ['quantity', 'foodName']
        
        



    