from django.views import View
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, LoginForm
from customuser.models import CustomUser


class LoginView(View):
    html = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.html, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(email=data['email'], password=data['password'])
                login(request, user)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    return HttpResponseRedirect("login/")
        return render(request, self.html, {'form': form})


class SignupView(View):
    html = 'signup.html'
    form_class = CustomUserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.html, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = CustomUser.objects.create_user(
                data['email'],
                data['password1']
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))
            
        else:
            return render(request, self.html, {'form': form})


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(('/login/'))


def main_view(request):
    html = "main.html"
    return render(request, html)


def company_less_view(request):
    html = "company_less.html"
    return render(request, html, {'context': "theContext"})


def company_more_view(request):
    html = "company_more.html"
    return render(request, html, {'context': "theContext"})


def buy_view(request):
    html = "buy.html"
    return render(request, html, {'context': "theContext"})


def fundamental_analysis_view(request):
    html = "fundamental_analysis.html"
    return render(request, html, {'context': "theContext"})
