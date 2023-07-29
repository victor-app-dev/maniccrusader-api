from django.shortcuts import render
from rest_framework import viewsets
import requests
from django.http import JsonResponse
import os
import json
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
def getCountires(request):
    key = os.environ.get("STORE_TOKEN")
    headers = {'Authorization': f'Bearer {key}'}
    url = f'https://api.printful.com/countries'
    response = requests.get(url, headers=headers)
    return JsonResponse(response.json())
# def getShippingDetails(request, payload):
#     key = os.environ.get("STORE_TOKEN")
#     headers = {'Authorization': f'Bearer {key}'}
#     url = 'https://api.printful.com/shipping/rates'
#     payload_dict = json.loads(payload)
#     response = requests.post(url, headers=headers, json=payload_dict)
#     return JsonResponse(response.json())

def getShippingDetails(request):
    # Retrieve the API key securely, using environment variables or Django settings
    key = os.environ.get("STORE_TOKEN")

    if not key:
        return JsonResponse({"error": "API key not available."}, status=500)

    # Ensure that the view function only responds to POST requests
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method."}, status=405)

    try:
        # Get the payload from the request body
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON payload."}, status=400)

    url = 'https://api.printful.com/shipping/rates'
    headers = {'Authorization': f'Bearer {key}'}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()

        # Check if the response contains an error
        if "error" in response_data:
            return JsonResponse(response_data, status=response.status_code)

        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": "Error making API request.", "details": str(e)}, status=500)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Error parsing API response."}, status=500)