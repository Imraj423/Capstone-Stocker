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

#alphaVantage api
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import json
# from matplotlib.pyplot import figure
# import matplotlib.pyplot as plt


def csrf(request):
    print(str(request))
    # print(request.query_params)
    repr(request)
    return JsonResponse({'csrfToken': get_token(request)})


def ping(request):
    return JsonResponse({'result': 'OK'})


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('-name')
    serializer_class = StockSerializer

    @action(detail=True, methods=['GET', 'POST'])
    def search(self, request, *args, **kwargs):
        '''http://localhost:8000/api/stocks/{pk or search}/search'''
        print(request, args, kwargs)

        # --API_KEY = 'HV9B9WY1I8NHBYU1'
        key = 'HV9B9WY1I8NHBYU1'
        # --Chose your output format, or default to JSON (python dict)
        # ts = TimeSeries(key, output_format='pandas')
        ts = TimeSeries(key)

        ti = TechIndicators(key)

        # --Get the data, returns a tuple
        # --aapl_data is a pandas dataframe, aapl_meta_data is a dict
        aapl_data, aapl_meta_data = ts.get_daily(symbol='AAPL')
        # aapl_sma is a dict, aapl_meta_sma also a dict
        aapl_sma, aapl_meta_sma = ti.get_sma(symbol='AAPL')
        # --Visualization
        # figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
        # aapl_data['4. close'].plot()
        # plt.tight_layout()
        # plt.grid()
        # plt.show()
        result = json.dumps(aapl_data)
        print(json.dumps(aapl_data))

        return JsonResponse({"result": result})