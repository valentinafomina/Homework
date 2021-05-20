from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm


def login(request):
    title = 'Вход'

    login_form = ShopUserLoginForm(data=request.POST)
    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('mainapp:index'))

    context = {
        'title': title,
        'login_form':login_form,
        'next' : next
    }
    return render(request, 'authapp/login.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))


def register(request):
    title = 'регистрация'

    if request.method:
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {'title':title, 'register_form':register_form}

    return render(request, 'authapp/register.html', content)


def edit(request):
    title = 'редактировать'

    if request.method:
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserRegisterForm(instance=request.user)

    content = {'title':title, 'edit_form':edit_form}

    return render(request, 'authapp/edit.html', content)



