from django.db import models


class Category(models.Model):
    Category_name = models.CharField(max_length=20)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.Category_name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
