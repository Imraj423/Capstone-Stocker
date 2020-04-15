from django.contrib import admin
from django.urls import path, include
from portfolio.views import search, news, keyword, crypto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landingpage.urls')),
    path('', include('customuser.urls')),
    path('search/<str:symbol>/', search),
    path('news/<str:symbol>/', news),
    path('keyword/<str:keyword>/', keyword),
    path('crypto/', crypto)


]