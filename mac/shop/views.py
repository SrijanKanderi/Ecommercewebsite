from django.http import HttpResponse
from .models.products import Product
from django.shortcuts import render


def index(request):
    Products = Product.get_all_objects()
    context = {'Products': Products}
    return render(request,'index.html', context)

def aboutus(request):
    return render(request, 'nav.html')
