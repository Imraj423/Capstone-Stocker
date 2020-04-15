# from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.http import JsonResponse, HttpRequest
from .models import Stock

import json
# import gzip

def search(request, symbol):
    '''GET http://localhost:8000/search/aapl/ => substitute 'aapl' for any other ticker symbol only
        Function returns ticker symbol, open, high, low, price, volume available, previous close, change
        amt and change percentage.'''
    key = 'HV9B9WY1I8NHBYU1'
    query = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={key}'
    r = requests.get(query)
    return JsonResponse({'result': r.json()})

def news(request, symbol):
        '''GET http://localhost:8000/news/aapl/ => get news info by ticker symbol or company name'''
        key = 'Tsk_9dda15a9c6a246d2a7022395b7aa8b90'
        query = f'https://sandbox.iexapis.com/stable/stock/AAPL/news/last/3/?token={key}'
        # query = f'https://sandbox.iexapis.com/stable/stock/AAPL/batch?types=quote,stats,company,news,chart&range=1y&token={API_KEY}'
        r = requests.get(query)
        return JsonResponse({'result': r.json()})

def keyword(request, keyword):
        '''GET http://localhost:8000/keyword/microsoft/ => substitute 'sony' for any other company name or ticker symbol
            This function takes any keyword or symbol and returns an array of possible matches.  We likely only need option 1 (symbol)
            and 2 (name) from each of the matches.'''
        key = 'HV9B9WY1I8NHBYU1'
        query = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={key}'
        r = requests.get(query)
        data = r.json()['bestMatches']
        return JsonResponse({'result': data})

def crypto(request):
        '''GET http://localhost:8000/api/stocks/crypto/crypto/ => Will wire up to take multiple kwargs for queries below.
            Currently returns daily value, index health, and exchange rates.'''
        if (request.method == 'GET'):
            key = 'HV9B9WY1I8NHBYU1'
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
