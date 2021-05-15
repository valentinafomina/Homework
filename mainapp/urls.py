from django.urls import path
from .views import main, products, contacts
from .urls import main

urlpatterns = [
    path('', main, name='index'),
    path('index/', main, name='index'),
    path('products/', products, name='products'),
    path('contact/', contacts, name='contact')
]

app_name = 'mainapp'