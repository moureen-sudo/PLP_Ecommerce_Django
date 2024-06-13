from django.shortcuts import render
from .models import Product


# Create your views here.
def product_list(request):
    product = Product.objects.all()
    context = {
        'products': product
    }
    return render(request, 'plp_ecommerce/product_list.html',context)

