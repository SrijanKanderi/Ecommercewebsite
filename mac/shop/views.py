from django.http import HttpResponse
from .models.products import Product
from django.shortcuts import render
from .models.categories import Category


def index(request):
    Products = None
    Categories = Category.get_all_categories()
    CategoryID= request.GET.get('Category')
    if CategoryID:
        Products = Product.get_all_product_by_category_id(CategoryID)
    else:
        Products = Product.get_all_objects()

    context = {'Products': Products, 'Categories': Categories}
    return render(request,'index.html', context)


def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    
    else:
        print(request.POST)
        return HttpResponse("I AM GAY")

    






