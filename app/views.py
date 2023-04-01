from django.shortcuts import render
from rest_framework import viewsets
#import serializers clases
#import models classes
# Create your views here.
def home_page(request):
      
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "home.html")