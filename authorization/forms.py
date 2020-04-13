from django import forms
# from django.contrib.auth.forms import UserCreationForm


class SignupForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4,
                               max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)
