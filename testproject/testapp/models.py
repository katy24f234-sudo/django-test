from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField # pyright: ignore[reportMissingImports]

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/',default='default.jpg')
    def __str__(self):
        return self.title
    
class CustomProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    address=models.CharField(max_length=220)
    phone_number=PhoneNumberField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=220)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/',default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    def __str__(self):
        return self.name  

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    @property
    def item_count(self):
        return sum(item.quantity for item in self.items.all())
    @property
    def total(self):
        return sum(item.total for item in self.items.total.all())
    def __str__(self):
        return f"{self.user.username} cart"

class Cartitem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_items')
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    quantity=models.PositiveIntegerField(default=1) 
    @property
    def total(self):
        return self.product.price * self.quantity
    def __str__(self):
        return self.product.name