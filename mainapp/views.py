from django.shortcuts import render
from .models import Product, ProductCategory


def main(request):
    products = Product.objects.all()[:4]

    context = {
        'title': 'Очень удобные стулья',
        'topic': 'Тренды',
        'products': products
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request):

    links_menu = {'links': [
            {'href': 'mainapp:index', 'name': 'все'},
            {'href': 'mainapp:index', 'name': 'дом'},
            {'href': 'mainapp:index', 'name': 'офис'},
            {'href': 'mainapp:index', 'name': 'модерн'},
            {'href': 'mainapp:index', 'name': 'классика'}
        ]}
    return render(request, 'mainapp/products.html', context=links_menu)


def contacts(request):
    return render(request, 'mainapp/contact.html')







# Create your views here.
