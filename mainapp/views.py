from django.shortcuts import render


def main(request):
    context = {
        'title': 'Очень удобные стулья',
        'topic': 'Тренды'
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request):

    links_menu = {'links': [
            {'href': 'index', 'name': 'все'},
            {'href': 'index', 'name': 'дом'},
            {'href': 'index', 'name': 'офис'},
            {'href': 'index', 'name': 'модерн'},
            {'href': 'index', 'name': 'классика'}
        ]}
    return render(request, 'mainapp/products.html', context=links_menu)


def contacts(request):
    return render(request, 'mainapp/contact.html')







# Create your views here.
