from django.shortcuts import render
import requests
from requests import Request, Session
import json
from django.views import View


def index(request):
    return render(request, 'index.html', {})


class CryptoCurrencyDetails(View):
    def get(self, request=None):
        """Get the details of all the crypto currency prices"""
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        # https: // pro - api.coinmarketcap.com / v1 / cryptocurrency / trending / latest
        parameters = {
            'start': '1',
            'limit': '5',
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'b038c056-0bbd-473c-b080-7abf41a0b36b',
        }
        try:
            response = requests.get(url, params=parameters,headers=headers)
            responseAPI = json.loads(response.text)['data']
            final = []
            for eachResponse in responseAPI:
                final.append({'name':eachResponse['name'],
                              'rank':eachResponse['cmc_rank'], 'symbol':eachResponse['symbol'],
                              'price':eachResponse['quote']['USD']['price']})
            return render(request, 'list.html', {'data':final})
        except Exception as e:
            print(e)
            return render(request, 'list.html', {})

class CurrencyPriceDetails(View):
    def get(self, request=None):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?date_added="2013-04-28T00:00:00.000Z"'
        # https: // pro - api.coinmarketcap.com / v1 / cryptocurrency / trending / latest
        parameters = {
            'start': '1',
            'limit': '5',
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'b038c056-0bbd-473c-b080-7abf41a0b36b',
        }
        try:
            response = requests.get(url, params=parameters, headers=headers)
            responseAPI = json.loads(response.text)
            print(responseAPI)
            final = []
            for eachResponse in responseAPI:
                final.append({'name': eachResponse['name'],
                              'rank': eachResponse['cmc_rank'], 'symbol': eachResponse['symbol'],
                              'price': eachResponse['quote']['USD']['price']})
            return render(request, 'priceList.html', {'data': final})
        except Exception as e:
            print(e)
            return render(request, 'priceList.html', {})


