from .models import CustomUser
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect


def login_view(request):
    html = "genericForm.html"
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                email=data["email"],
                password=data["password"])
            if user:
                login(request, user)
                return redirect(request.GET.get("next", "/"))
            else:
                return HttpResponseRedirect("invalid authentication")
    form = LoginForm()
    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def register_view(request):
    html = "genericForm.html"
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                email=data["email"],
                password=data["password1"]
            )
            login(request, user)
            return redirect(reverse('login'))
    form = CustomUserCreationForm()
    return render(request, html, {'form': form})