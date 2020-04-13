from django.db import models
from django.utils import timezone
import random


class Stock(models.Model):
    s_id = models.IntegerField(default=random.randint(0, 999999), unique=True, editable=False)
    ticker_symbol = models.CharField(blank=False, max_length=5, unique=True)
    # change to feed direct from api
    name = models.CharField(blank=False, max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    up = models.BooleanField(default=False)
    down = models.BooleanField(default=False)
    variance_percentage = models.DecimalField(max_digits=3, decimal_places=3, blank=False, default=0)
    variance_USD = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0.00)
    # change to user foreign key.  This will be a list of folks who own shares
    shareholders = models.CharField(default='null', max_length=50)
    date = models.DateField(auto_now=True)
    # change to user.id foreign key.  This will be a list of folks who own shares
    followers = models.CharField(max_length=50, default='null')

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    p_id = models.IntegerField(default=random.randint(0, 999999), unique=True, editable=False)
    # change to user.id foreign key.  This will be a list of folks who own shares
    user = models.CharField(blank=False, max_length=50)
    # change to stock's u_id.  This will be a list of stocks the user owns
    stocks_held = models.CharField(blank=False, max_length=2000, default=None)
    # change to dictionary foreign key with stock info needed to yield variance detail
    stock_detail = models.CharField(blank=False, max_length=2000)
    status = models.CharField(choices=[('B', 'buy'), ('S', 'sell'), ('T', 'trade'), ('H', 'hold')], blank=False, max_length=1, default='H')
    up = models.BooleanField(default=False)
    down = models.BooleanField(default=False)
    total_invested = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0.00)
    total_variance_percentage = models.DecimalField(max_digits=3, decimal_places=2, blank=False, default=0.00)
    total_variance_USD = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0.00)
    time_frame = models.CharField(choices=[('D', '1-day'), ('M', '1-month'), ('Y', '1-year'), ('5', '5-years')], blank=False, max_length=1, default='D')

    def __str__(self):
        # change this to f'self.p_id - self.user.last, self.user.first'
        return self.user




