from django.shortcuts import render

from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from .models import Stock


class StockListView(ListView):
    template_name = 'stock/stock_home_page.html'
    queryset = Stock.objects.all()
    
    

