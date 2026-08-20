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
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True,related_name='cart')
    session_key=models.CharField(max_length=50,null=True,blank=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    @property
    def item_count(self):
        return sum(item.quantity for item in self.items.all())
    @property
    def total(self):
        return sum(item.total for item in self.items.all())
    def __str__(self):
        return  f"cart {self.id}"

class Cartitem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_items')
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    quantity=models.PositiveIntegerField(default=1) 
    @property
    def total(self):
        return self.product.price * self.quantity
    def __str__(self):
        return self.product.name

class Order(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        CONFIRMED = 'CONFIRMED', 'Confirmed'
        SHIPPED = 'SHIPPED', 'Shipped'
        DELIVERED = 'DELIVERED', 'Delivered'
        CANCELLED = 'CANCELLED', 'Cancelled'
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )
    total=models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    upadated_at=models.DateTimeField(auto_now=True) 
    receipt_image = models.ImageField(upload_to='images/receipts/',blank=True,null=True)
    def __str__(self):
        return f"{self.user.username} order"

class Orderitem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    name=models.CharField(max_length=50)
    quantity=models.PositiveIntegerField() 
    price=models.DecimalField(max_digits=10, decimal_places=2)
    total=models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name