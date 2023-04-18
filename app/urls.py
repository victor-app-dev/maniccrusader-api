from django.urls import path
from .views import home_page, getStores, getProducts,getProducts_details,getProducts_tshirts,getProducts_hoodies,getProducts_hats, getVariant_details

urlpatterns = [
    path('', home_page),
    path('api/stores/', getStores, name='get_Stores'),
    path('api/products/', getProducts, name='get_Products'),
    path('api/products-details/<int:product_id>/', getProducts_details, name='get_Products_details'),
    path('api/products-tshirts/', getProducts_tshirts ),
    path('api/products-hoodies/', getProducts_hoodies),
    path('api/products-hats/', getProducts_hats),
    path('api/variant-details/<int:variant_id>/', getVariant_details)
]