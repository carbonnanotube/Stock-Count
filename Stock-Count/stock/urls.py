"""
Stock_Count URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from stock.views import StockListView, update , StockCreate, reporting, generate_report

from stock import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [

  path('', StockListView, name = 'stock_view' ),
  path('update', update, name = 'update'),
  path('create', StockCreate.as_view(), name = 'create'),
  path('report', reporting, name = 'stock_report'),
  path('generate_report', generate_report, name='generate_report'),
  
  
 
]

urlpatterns += staticfiles_urlpatterns()