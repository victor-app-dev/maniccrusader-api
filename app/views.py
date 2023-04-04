from django.shortcuts import render
from rest_framework import viewsets
import requests
from django.http import JsonResponse
import os
#import serializers clases
#import models classes
# Create your views here.
def home_page(request):
    return render(request, "home.html")

def getStores(request):
    key = os.environ.get("STORE_TOKEN")
    headers = {'Authorization': f'Bearer {key}'}
    url = 'https://api.printful.com/stores'
    response = requests.get(url, headers=headers)
    return JsonResponse(response.json())