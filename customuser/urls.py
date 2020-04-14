from django.urls import path
from . import views

urlpatterns = [
    
    path('signup/', views.SignupView.as_view(), name='register'),
    path("login/", views.LoginView.as_view(), name="login"),
    path('logout/', views.logoutUser, name='logout'),
    path('main/', views.main_view, name='main'),
    path('buy/', views.buy_view, name='buy'),
    path('company/', views.company_more_view, name='company'),
    path('analysis/', views.fundamental_analysis_view, name='analysis')
]