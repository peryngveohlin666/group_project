from django.http import HttpResponse
from django.shortcuts import render


#don't forget to add the templates folder in setting.py
def index(request):
    return render(request, "index.html")