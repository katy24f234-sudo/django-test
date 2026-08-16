from django.contrib import admin
from .models import Post ,CustomProfile,Product,Cart,Cartitem

admin.site.register(Post)
admin.site.register(CustomProfile)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Cartitem)