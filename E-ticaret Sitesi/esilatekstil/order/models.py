from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.forms import ModelForm , TextInput
# Create your models here.

class ShopCart(models.Model):
    user = models.ForeignKey( User , on_delete = models.SET_NULL , null = True)
    product = models.ForeignKey( Product , on_delete = models.SET_NULL , null = True)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)


    def __str__(self):
       return str(self.product)
    
    @property
    def amount(self):
        return(self.quantity * self.product.price)
    
    @property
    def price(self):
        if self.product and self.product.price:
            return self.product.price
        else:
            return None # veya başka bir varsayılan fiyat değeri

    

class ShopCartForm(ModelForm):
    class Meta :
        model = ShopCart
        fields = ['quantity']
        
