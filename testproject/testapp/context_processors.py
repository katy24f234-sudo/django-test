from .models import Cart,Cartitem

def cart_context(request):
    if not request.user.is_authenticated:
        if request.session.session_key is None:
            request.session.create()
        cart_session_key=request.session.session_key
        cart,_=Cart.objects.get_or_create(session_key=cart_session_key)
        itemcount=cart.item_count
        request.session["cart_session_key"]=cart_session_key

    else:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        if request.session["cart_session_key"] is not None:
            session_cart,_=Cart.objects.get_or_create(session_key=request.session["cart_session_key"])
            for item in session_cart.items.all():
                cartitem,created=Cartitem.objects.get_or_create(cart=cart,product=item.product)
                if created:
                    cartitem.quantity=item.quantity
                else:
                    cartitem.quantity+=item.quantity
                cartitem.save()

            session_cart.delete()
        # itemcount = cart.item_count

    return {
        "cart": cart,
    }