from django.urls import path
from .views import home_page, getStores

urlpatterns = [
    path('', home_page),
    path('api/stores/', getStores, name='getStores')
]