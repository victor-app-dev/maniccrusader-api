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

def getProducts(request):
    key = os.environ.get("STORE_TOKEN")
    headers = {'Authorization': f'Bearer {key}'}
    url = 'https://api.printful.com/store/products'
    response = requests.get(url, headers=headers)
    return JsonResponse(response.json())

def getProducts_details(request, product_id):
    key = os.environ.get("STORE_TOKEN")
    headers = {'Authorization': f'Bearer {key}'}
    url = f'https://api.printful.com/store/products/{product_id}'
    response = requests.get(url, headers=headers)
    return JsonResponse(response.json())
def getProducts_tshirts(request):
    key = os.environ.get("STORE_TOKEN")
    headers = {'Authorization': f'Bearer {key}'}
    url = 'https://api.printful.com/store/products?category_id=24'
    response = requests.get(url, headers=headers)
    return JsonResponse(response.json())
def getProducts_hoodies(request):
    key = os.environ.get("STORE_TOKEN")
    headers = {'Authorization': f'Bearer {key}'}
    url = 'https://api.printful.com/store/products?category_id=7'
    response = requests.get(url, headers=headers)
    return JsonResponse(response.json())
def getProducts_hats(request):
    key = os.environ.get("STORE_TOKEN")
    headers = {'Authorization': f'Bearer {key}'}
    url = 'https://api.printful.com/store/products?category_id=15'
    response = requests.get(url, headers=headers)
    return JsonResponse(response.json())
def getVariant_details(request, variant_id):
    key = os.environ.get("STORE_TOKEN")
    headers = {'Authorization': f'Bearer {key}'}
    url = f'https://api.printful.com/store/variants/{variant_id}'
    response = requests.get(url, headers=headers)
    return JsonResponse(response.json())