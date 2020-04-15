from django.contrib import admin
from django.urls import path, include
from portfolio.views import StockViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'stocks', StockViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landingpage.urls')),
    path('', include('customuser.urls')),
    path('api/', include(router.urls))
]