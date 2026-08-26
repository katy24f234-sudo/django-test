from django.contrib import admin
from .models import Post ,CustomProfile,Product,Cart,Cartitem,Order,Orderitem
from modeltranslation.admin import TranslationAdmin # pyright: ignore[reportMissingImports]

admin.site.register(Post)

admin.site.register(CustomProfile)

admin.site.register(Cart)

admin.site.register(Cartitem)

admin.site.register(Order)

admin.site.register(Orderitem)

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    pass


# @admin.register(Order)
# class OrderAdmin(TranslationAdmin):
#     pass


# @admin.register(Orderitem)
# class OrderitemAdmin(TranslationAdmin):
#     pass