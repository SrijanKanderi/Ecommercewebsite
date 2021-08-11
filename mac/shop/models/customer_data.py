from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=14)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.email

