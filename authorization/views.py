from django.views import View
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User


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
                user = authenticate(username=data['username'], password=data['password'])
                login(request, user)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect("/")
        return render(request, self.html, {'form': form})


class SignupView(View):
    html = 'signup.html'
    form_class = SignupForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.html, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                data['username'],
                data['email'],
                data['password1']
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return render(request, self.html, {'form': form})


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/login/')
