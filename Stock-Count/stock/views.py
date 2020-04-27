from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import request
from django.http import HttpResponse


from django.views.generic import CreateView, DeleteView, UpdateView, ListView, View

from .models import Stock, Transaction
from .forms import StockForm


def StockListView(request):
    
    obj = Stock.objects.order_by('dateTime')
    
    context = {
        
        'obj' : obj,
        }

    return render(request, 'stock/stock_home_page.html', context)



    
  
def update(request):
    context = None


    if request.method == 'POST':
        obj = request.POST
       
        for k, v in obj.items():

            key = ''.join(i for i in k if i.isdigit()) 
            value = ''.join(i for i in v if i.isdigit())
            
            # I control the key value as it's the ID data from the database, but need to verify the use input value
            if key.isdigit() and value.isdigit():
                tempKey = int(key)
                tempValue = int(value)

                if tempValue > 0:  

                    temp = Stock.objects.get(pk = tempKey)
                    temp.quantity = tempValue

                    # temp value, I couldn't pass number as the requirement was Stock object, and temp has the value with correct PK
                    transaction = Transaction(stock = temp, quantity = tempValue)

                    transaction.save()
                    temp.save()
                

        # only redirect once loop has run through all value, key in the object from the form data
        return redirect('stock_view')
        


class StockCreate(CreateView):
    model = Stock

    fields = ['foodName']
    template_name = 'stock/stock_create_page.html'

    success_url = '/'
 
    


def reporting(request):

    
    all_transactions = Transaction.objects.all()

    # from the Stock table returns unique names 
    unique_product_name = Stock.objects.all() #.values('foodName').distinct()

    context = {        
        'all_transactions' : all_transactions,
        'product_name' : unique_product_name,
        }
    

    return render(request, 'stock/stock_report_page.html', context)


