# from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework import viewsets, serializers
from .serializers import StockSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse, HttpRequest
from .models import Stock

# alphaVantage api
# from alpha_vantage.timeseries import TimeSeries
# from alpha_vantage.techindicators import TechIndicators
import json
# import gzip


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('-name')
    serializer_class = StockSerializer

    @action(detail=True, methods=['GET', 'POST'])
    def search(self, request, *args, **kwargs):
        ''' GET http://localhost:8000/api/stocks/aapl/search/ => substitute 'aapl' for any other ticker symbol only
            Function returns ticker symbol, open, high, low, price, volume available, previous close, change amt and
            change percentage.'''
        if (request.method == 'GET'):
            key = 'HV9B9WY1I8NHBYU1'
            keyword = kwargs['pk']
            query = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={keyword}&apikey={key}'
            r = requests.get(query)
            data = r.json()
            return JsonResponse({'result': data})

    @action(detail=True, methods=['GET', 'POST'])
    def news(self, request, *args, **kwargs):
        '''GET http://localhost:8000/api/stocks/news/news/'''
        API_KEY = 'Tsk_9dda15a9c6a246d2a7022395b7aa8b90'
        query = f'https://sandbox.iexapis.com/stable/stock/AAPL/news/last/3/?token={API_KEY}'
        # query = f'https://sandbox.iexapis.com/stable/stock/AAPL/batch?types=quote,stats,company,news,chart&range=1y&token={API_KEY}'
        r = requests.get(query)
        return JsonResponse({'result': r.json()})

    @action(detail=True, methods=['GET', 'POST'])
    def keyword(self, request, *args, **kwargs):
        '''GET http://localhost:8000/api/stocks/sony/keyword/ => substitute 'sony' for any other company name or ticker symbol
            This function takes any keyword or symbol and returns an array of possible matches.  We likely only need option 1 (symbol)
            and 2 (name) from each of the matches.'''
        if (request.method == 'GET'):
            key = 'HV9B9WY1I8NHBYU1'
            keyword = kwargs['pk']
            query = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={key}'
            r = requests.get(query)
            data = r.json()['bestMatches']
            return JsonResponse({'result': data})

    @action(detail=True, methods=['GET', 'POST'])
    def crypto(self, request, *args, **kwargs):
        '''GET http://localhost:8000/api/stocks/crypto/crypto/ => Will wire up to take multiple kwargs for queries below.
            Currently returns daily value, index health, and exchange rates.'''
        if (request.method == 'GET'):
            key = 'HV9B9WY1I8NHBYU1'
            keyword = kwargs['pk']
            query_exchange = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey={key}'
            exchange_rates = requests.get(query_exchange)
            data_exchange = exchange_rates.json()

            query_health = f'https://www.alphavantage.co/query?function=CRYPTO_RATING&symbol=BTC&apikey={key}'
            health_index = requests.get(query_health)
            data_health = health_index.json()

            query_daily= f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=CNY&apikey={key}'
            current_rate = requests.get(query_daily)
            data_daily = current_rate.json()

            return JsonResponse({
                'exchange_rate': data_exchange,
                'health_index': data_health,
                'daily_rate': data_daily})
