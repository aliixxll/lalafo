from django.shortcuts import render
from apps.settings.models import Setting
from apps.products.models import Product

# Create your views here.
def product_detail(request, id):
    setting = Setting.objects.latest('id')
    product = Product.objects.get(id = id)
    context = {
        'product' : product,
        'setting' : setting,
    }
    return render(request, 'single-product.html', context)