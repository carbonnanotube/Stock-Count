from django.contrib import admin

from stock.models import Stock, Transaction


admin.site.register(Stock)
admin.site.register(Transaction)