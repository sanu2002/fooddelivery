from .models import Cart
from menuapp.models import Fooditem

def get_cart_counter(request):
    cart_count=0
    if request.user.is_authenticated:
        try:
            cart_item=Cart.objects.filter(user=request.user)
            print(cart_item)
            if cart_item:
                 for cart_item in cart_item:
                     cart_count+=cart_item.quantitiy
                     
            else:
                cart_count=0
                     
        except:
             cart_count=0
        
    return dict(cart_count=cart_count)


