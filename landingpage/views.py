from django.shortcuts import render
from .models import landingpage


def index(request):
    item = landingpage.objects.all()
    html = 'index.html'
    return render(request, html, {'data': item})
