from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/',default='default.jpg')
    def __str__(self):
        return self.title
    
# class CustomProfile(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
#     firstname=models.CharField(max_length=50)
#     lastname=models.CharField(max_length=50)
#     address=models.CharField(max_length=220)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.firstname} {self.lastname}"