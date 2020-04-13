from django.urls import path
from authorization import views
# from django.conf.urls import url

urlpatterns = [
    # path("signup/", authorization.views.signup_view, name="signup"),
    path('signup/', views.SignupView.as_view(), name='register'),
    path("login/", views.LoginView.as_view(), name="login"),
    path('logout/', views.logoutUser, name='logout'),
]
