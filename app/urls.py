from django.urls import path
from .views import home_page, getStores, getProducts,getProducts_details,getProducts_tshirts,getProducts_hoodies,getProducts_hats, getVariant_details, getCountires, getShippingDetails

urlpatterns = [
    path('', home_page),
    path('api/stores/', getStores, name='gets all stores associated with your account.'),
    path('api/products/', getProducts, name='gets all products from your store.'),
    path('api/products-details/<int:product_id>/', getProducts_details, name='gets product details, i.e. the variants etc.'),
    path('api/products-tshirts/', getProducts_tshirts),
    path('api/products-hoodies/', getProducts_hoodies ),
    path('api/products-hats/', getProducts_hats),
    path('api/variant-details/<int:variant_id>/', getVariant_details, name='gets variants details.'),
    path('api/countries/', getCountires, name='gets all countries you can ship to.'),
    path('api/shipping_rates/<str:payload>/', getShippingDetails, name='shipping_rates'),

]