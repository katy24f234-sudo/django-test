from .models import Cart

def cart_context(request):
    itemcount = 0

    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        itemcount = cart.item_count

    return {
        "itemcount": itemcount,
    }