from django.urls import path
from .views import home, products



urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
]


