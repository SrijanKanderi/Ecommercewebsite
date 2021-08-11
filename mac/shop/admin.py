
from django.contrib import admin
from .models.products import Product
from .models.categories import Category
from .models.customer_data import Customer


class Product_view(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'product_desc', 'category']

class Category_view(admin.ModelAdmin):
    list_display =['Category_name']


admin.site.register(Product, Product_view )
admin.site.register(Category, Category_view)
admin.site.register(Customer)
