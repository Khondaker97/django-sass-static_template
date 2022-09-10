from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'title': 'B2Brain Test','name' : 'Mahmud'})
