from modeltranslation.translator import register, TranslationOptions # pyright: ignore[reportMissingImports]
from .models import Product,Orderitem,Order


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
