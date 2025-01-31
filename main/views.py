from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from goods.models import Categories

def index(request):
    categories=Categories.objects.all()

    context= {
        'title': 'Kraft - головна',
        'content':'Магазин крафтових сирів і напоїв',
        'categories': categories,
    }
    return render(request,'main/index.html',context )

def about(request):
    context = {
        'title': 'Kraft - Про нас',
        'content': "Про нас",
        'text_on_page': 'Чому наша продукція така добра.'
    }
    return render(request, 'main/about.html', context)


def delivery_payment(request):
    context = {
        'title': 'Оплата і доставка',
        'content': "Оплата і доставка",
        'text_on_page': 'Про оплату і доставку.'
    }
    return render(request, 'main/delivery_payment.html', context)

def contacts(request):
    context = {
        'title': 'Контакти',
        'content': "Наші контакти",
        'text_on_page': 'Контактна інформація.'
    }
    return render(request, 'main/contacts.html', context)
