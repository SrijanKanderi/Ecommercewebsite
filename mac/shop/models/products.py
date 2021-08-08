from django.db import models
from .categories import Category


class Product(models.Model):
    product_name = models.CharField(max_length=20)
    product_price = models.IntegerField()
    product_desc = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default = 1)
    product_image= models.ImageField(upload_to='shop')

    def __str__(self):
        return self.product_name

    @staticmethod
    def get_all_objects():
        return Product.objects.all()