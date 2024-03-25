from .models import Cart,Tax
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
    tax_dict={}
    if request.user.is_authenticated:
        cart_item=Cart.objects.filter(user=request.user)
        for item in cart_item:
            fooditem=Fooditem.objects.get(pk=item.fooditem.id)
            subtotal+=(fooditem.price*item.quantitiy)
        tax_details=Tax.objects.filter(is_active=True)
        for i in tax_details:
            tax_type=i.tax_type
            tax_percentage=i.tax_percentage
            tax_amount=round((tax_percentage*subtotal)/100,2)
            tax_dict.update({tax_type:{str(tax_percentage):tax_amount}})
        
        for key in tax_dict.values():
            for i in key.values():
                tax +=i
        # tax=sum(key for key in tax_dict.values() for  key in key.values())
        grandtotal=subtotal+tax
        
      

    return dict(subtotal=subtotal,tax=tax,grandtotal=grandtotal,tax_dict=tax_dict)