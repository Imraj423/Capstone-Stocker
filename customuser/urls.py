from django.urls import path
from .views import register_view, login_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('join', register_view, name='join'),
    path('logout', logout_view, name='logout'),
]