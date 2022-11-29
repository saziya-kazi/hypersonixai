from django.contrib import admin
from django.urls import path
from . import views
from .views import CryptoCurrencyDetails, CurrencyPriceDetails

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', CryptoCurrencyDetails.as_view(), name='list'),
    path('prices/', CurrencyPriceDetails.as_view(), name='prices')
    #path('currencies', RouterDetails.as_view(), name='currencies'),
    ]