from django.contrib import admin
from .models import Post ,CustomProfile,Product,Cart,Cartitem,Order,Orderitem

admin.site.register(Post)
admin.site.register(CustomProfile)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Cartitem)
admin.site.register(Orderitem)
admin.site.register(Order)