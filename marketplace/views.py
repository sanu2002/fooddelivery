from django.shortcuts import redirect, render,HttpResponse
from django.http import JsonResponse
# Create your views here.
from django.db.models import Prefetch
from .models import Cart
from .context_processor import get_cart_counter


from menuapp.models import *

from django.shortcuts import get_object_or_404

from vendor.models import *

from accounts.models import Userprofile


def marketplace(request):
    vendor=Vendor.objects.all()
    userprofile=Userprofile.objects.all()
    # for i in vendor:
    #     print(i.user_profile.profile_pictutre)
    
    context={
        'vendor':vendor,
        'profile':userprofile
    }
    
    
    
    return render(request, 'market/marketplace.html',context)

def vendor_details(request,vendor_slug):
    vendor=get_object_or_404(Vendor,vendor_slug=vendor_slug)

    
    category=Category.objects.filter(vendor=vendor).prefetch_related(
        Prefetch(
            'fooditem',
            queryset=Fooditem.objects.filter(is_avalable=True)
        )
        
    )
    
    if request.user.is_authenticated:
        cart_item=Cart.objects.filter(user=request.user)
        
    else:
        cart_item=None
    
    context={
        'vendor':vendor,
        'category':category,
        'cart_item':cart_item,
    }
    
    
    return render(request,'market/vendor_details.html',context)



def add_to_cart(request, food_id):
    print(food_id)
    if request.user.is_authenticated:
        try:
            fooditem = Fooditem.objects.get(id=food_id)
            
            try:
                chckcart = Cart.objects.get(user=request.user, fooditem=fooditem)
                chckcart.quantitiy += 1
                chckcart.save()
                return JsonResponse({'status': 'increases cart','cart_count':get_cart_counter(request),'chckcart':chckcart.quantitiy})

            except Cart.DoesNotExist:
                chckcart = Cart.objects.create(user=request.user, fooditem=fooditem, quantitiy=1)
                chckcart.save()
                return JsonResponse({'status': 'new cart is created successfully','cart_count':get_cart_counter(request),'chckcart':chckcart.quantitiy})

        except Cart.DoesNotExist:
            return JsonResponse({'status': 'fooditem not found'})

    else:
        return JsonResponse({'status': 'You need to login'})
    
    
def remove_from_cart(request,food_id):
    if request.user.is_authenticated:
        try:
            fooditem = Fooditem.objects.get(id=food_id)
            
            try:
                chckcart = Cart.objects.get(user=request.user, fooditem=fooditem)
                if chckcart.quantitiy >1:
                    chckcart.quantitiy -= 1
                    chckcart.save()
                else:
                    chckcart.delete()
                    chckcart.quantitiy=0
                    
                return JsonResponse({'status': 'increases cart','cart_count':get_cart_counter(request),'chckcart':chckcart.quantitiy})



            except Cart.DoesNotExist:
                return JsonResponse({'status': 'failed','message':'you dont have item in this cart'})

                
               
        except Cart.DoesNotExist:
            return JsonResponse({'status': 'failed','message':'invalid-request'})

    else:
        return JsonResponse({'status': 'You need to login'})
    
    
    
  