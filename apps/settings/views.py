from django.shortcuts import render
from apps.settings.models import Setting
from apps.products.models import Product
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    try:
        setting = Setting.objects.latest('id')
    except:
        return HttpResponse("Добавь настройки проекта с админ панели")
    products = Product.objects.all()
    context = {
        'setting' : setting,
        'products' : products,
    }
    return render(request, 'index-1.html', context)

def product_detail(request, id):
    setting = Setting.objects.latest('id')
    product = Product.objects.get(id = id)
    context = {
        'product' : product,
        'setting' : setting,
    }
    return render(request, 'single-product.html', context)