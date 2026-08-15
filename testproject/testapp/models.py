from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

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