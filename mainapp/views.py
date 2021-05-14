from django.shortcuts import render
from .models import Product, ProductCategory
from django.shortcuts import get_object_or_404

from ..basketapp.models import Basket


def product(request, pk=None):
    title = 'продукты'

    categories = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name':'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category_if__pk=pk).order_by('price')

    context = {
        'title': title,
        'categories': categories,
        'category' : category,
        'products' : products
    }

    return render(request, 'products_list.html', context=context)

def main(request):
    products = Product.objects.all()[:4]
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': 'Очень удобные стулья',
        'topic': 'Тренды',
        'products': products,
        'basket' : basket,
    }
    return render(request, 'mainapp/index.html', context=context)


# def products(request, pk=None):
#     print(pk)
#
#     title = 'продукты'
#     links_menu = ProductCategory.objects.all()
#
#     if pk is not None:
#         if pk == 0:
#             products = Product.objects.all().order_by('price')
#             category = {'name': 'все'}
#         else:
#             category = get_object_or_404(ProductCategory, pk=pk)
#             products = Product.objects.filter(category__pk=pk).order_by('price')
#
#         content = {
#             'title': title,
#             'links_menu': links_menu,
#             'category': category,
#             'products': products,
#         }
#
#         return render(request, 'mainapp/products_list.html', content)
#
#     same_products = Product.objects.all()[3:5]
#
#     content = {
#         'title': title,
#         'links_menu': links_menu,
#         'same_products': same_products
#     }
#
#     return render(request, 'mainapp/products.html', content)
#
#
# def contacts(request):
#     return render(request, 'mainapp/contact.html')







# Create your views here.
