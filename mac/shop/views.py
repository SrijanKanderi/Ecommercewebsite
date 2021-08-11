from os import error
from django.http import HttpResponse
from .models.products import Product
from django.shortcuts import render, redirect
from .models.categories import Category
from .models.customer_data import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

class index(View):
    def get(self,request):
        Products = None
        Categories = Category.get_all_categories()
        CategoryID= request.GET.get('Category')
        if CategoryID:
            Products = Product.get_all_product_by_category_id(CategoryID)
        else:
            Products = Product.get_all_objects()

        context = {'Products': Products, 'Categories': Categories}
        print("you are:", request.session.get('customer_email'))
        return render(request,'index.html', context)
    
    def post(self,request):
        flag = request.POST.get("productid")
        print(flag)
        return HttpResponse("Test")

class signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self,request):
        first_name = request.POST.get("firstname")
        last_name= request.POST.get("lastname")
        phone= request.POST.get("phone")
        email= request.POST.get("email")
        password= make_password(request.POST.get("password"))
        customer = Customer(first_name = first_name, last_name=last_name, phone=phone, email=email, password = password)
        
        if customer.isExists():
            return HttpResponse("email address already exists!")


        else:
            customer.register()

        return redirect('http://localhost:8000')

class signin(View):
    def get(self, request):
        return render(request, 'signin.html')


    def post(self,request):
        email = request.POST.get("login_email")
        password = request.POST.get("login_password")
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email

                return redirect('http://localhost:8000');
            else:
                error_message="Email or Password invalid"
        else:
            error_message="Email or Password invalid"
        print(request.session)
        return render(request,'signin.html',{"error":error_message})


def signout(request):

    request.session.flush()
    
    return redirect('http://localhost:8000')



    
    
    

    
    


