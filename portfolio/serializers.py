from rest_framework import serializers
from .models import Stock, Portfolio


class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 's_id', 'ticker_symbol', 'name', 'price', 'up', 'down', 'variance_percentage', 'variance_USD', 'shareholders', 'date']


class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['p_id', 'user', 'stocks_held', 'stock_detail', 'status', 'up', 'down', 'total_invested', 'total_variance_percentage', 'total_variance_USD', 'time_frame']