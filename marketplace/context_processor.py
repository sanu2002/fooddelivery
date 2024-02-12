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






def get_cart_amont(request):
    subtotal=0
    tax=0
    grandtotal = 0
    if request.user.is_authenticated:
        cart_item=Cart.objects.filter(user=request.user)
        for item in cart_item:
            fooditem=Fooditem.objects.get(pk=item.fooditem.id)
            subtotal+=(fooditem.price*item.quantitiy)
        
        grandtotal=subtotal + tax
        
    print(subtotal)
    print(grandtotal)
        
    return dict(subtotal=subtotal,tax=tax,grandtotal=grandtotal)