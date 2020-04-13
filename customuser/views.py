# from .models import CustomUser
# from .forms import CustomUserCreationForm, LoginForm
# from django.contrib.auth import login, authenticate, logout
# from django.shortcuts import render, redirect, reverse, HttpResponseRedirect


# def login_view(request):
#     html = "login.html"
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(
#                 email=data["email"],
#                 password=data["password"])
#             if user:
#                 login(request, user)
#                 return redirect(request.GET.get("next", "/"))
#             else:
#                 return HttpResponseRedirect("invalid authentication")
#     form = LoginForm()
#     return render(request, html, {'form': form})


# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('login'))


# def register_view(request):
#     html = "genericForm.html"
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = CustomUser.objects.create_user(
#                 email=data["email"],
#                 password=data["password1"]
#             )
#             login(request, user)
#             return redirect(reverse('login'))
#     form = CustomUserCreationForm()
#     return render(request, html, {'form': form})


from django.views import View
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.models import User
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
