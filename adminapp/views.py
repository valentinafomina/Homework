from django.contrib.auth.decorators import user_passes_test

from authapp.models import ShopUser
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from mainapp.models import Product, ProductCategory

from geekshop.adminapp.forms import ShopUserAdminEditForm
from geekshop.authapp.forms import ShopUserRegisterForm


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = '�������/������������'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', context=context)


def user_create(request):
    pass
    # title = '�������� ������������'
    #
    # if request.method == 'POST':
    #     user_form = ShopUserRegisterForm(request.POST, request.FILES)
    #     if user_form.is_valid():
    #         user_form.save()
    #         return HttpResponseRedirect(reverse('admin:users'))
    # else:
    #     user_form = ShopUserRegisterForm()
    #
    # context = {'title': title, 'update_form': user_form}
    #
    # return render(request, 'adminapp/user_update.html', context)



def user_update(request, pk):
    pass
    # title = '�������������� ������������'
    #
    # edit_user = get_object_or_404(ShopUser, pk=pk)
    # if request.method == 'POST':
    #     edit_form = ShopUserAdminEditForm(request.POST, request.FILES, \
    #                                       instance=edit_user)
    #     if edit_form.is_valid():
    #         edit_form.save()
    #         return HttpResponseRedirect(reverse('admin:user_update', \
    #                                             args=[edit_user.pk]))
    # else:
    #     edit_form = ShopUserAdminEditForm(instance=edit_user)
    #
    # context = {'title': title, 'update_form': edit_form}
    #
    # return render(request, 'adminapp/user_update.html', context)


def user_delete(request, pk):
    pass
    # title = '������������/��������'
    #
    # user = get_object_or_404(ShopUser, pk=pk)
    #
    # if request.method == 'POST':
    #     user.delete()
    #     # user.is_active = False
    #     user.save()
    #     return HttpResponseRedirect(reverse('admin:users'))
    #
    # context = {'title': title, 'user_to_delete': user}
    #
    # return render(request, 'adminapp/user_delete.html', context)


def categories(request):
    title = '�������/���������'

    categories_list = ProductCategory.objects.all()

    context = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', context)


def category_create(request):
    pass


def category_update(request, pk):
    pass


def category_delete(request, pk):
    pass


def products(request, pk):
    title = '�������/�������'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)


def product_create(request, pk):
    pass


def product_read(request, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass