from django.shortcuts import redirect, render,HttpResponse
from django.http import JsonResponse
# Create your views here.
from django.db.models import Prefetch
from .models import Cart
from .context_processor import get_cart_counter,get_cart_amont

from django.db.models import Q
from datetime import date,datetime



from django.contrib.auth.decorators import login_required


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

    
    opening_hour=Openinghour.objects.filter(vendor=vendor).order_by('day','-from_hour')
    # print(opening_hour)
    # for i in opening_hour:
    #     print(i.from_hour,i.to_hour)
    today=date.today().isoweekday()
    current_openignday=Openinghour.objects.filter(vendor=vendor,day=today)
    


    

    
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
        'opening_hour':opening_hour,
        'current_openignday':current_openignday
    }
    
    
    return render(request,'market/vendor_details.html',context)



def add_to_cart(request, food_id):
    if request.user.is_authenticated:
            try:
                fooditem = Fooditem.objects.get(id=food_id)
                
                try:
                    chckcart = Cart.objects.get(user=request.user, fooditem=fooditem)
                    chckcart.quantitiy += 1
                    chckcart.save()
                    return JsonResponse({'status': 'increases cart', 'cart_count': get_cart_counter(request), 'chckcart': chckcart.quantitiy,'cart_amount':get_cart_amont(request)}, status=200)

                except Cart.DoesNotExist:
                    chckcart = Cart.objects.create(user=request.user, fooditem=fooditem, quantitiy=1)
                    chckcart.save()
                    return JsonResponse({'status': 'new cart is created successfully', 'cart_count': get_cart_counter(request), 'chckcart': chckcart.quantitiy}, status=200)

            except Fooditem.DoesNotExist:
                return JsonResponse({'status': 'fooditem not found'}, status=400)
        
    else:
        return JsonResponse({'status': 'login_required', 'message': 'you need to login first'}, status=401)

def remove_from_cart(request, food_id):
    if request.user.is_authenticated:
            try:
                fooditem = Fooditem.objects.get(id=food_id)
                
                try:
                    chckcart = Cart.objects.get(user=request.user, fooditem=fooditem)
                    if chckcart.quantitiy > 1:
                        chckcart.quantitiy -= 1
                        chckcart.save()
                    else:
                        chckcart.delete()
                        chckcart.quantitiy = 0
                        
                    return JsonResponse({'status': 'decreases cart', 'cart_count': get_cart_counter(request), 'chckcart': chckcart.quantitiy,'cart_amount':get_cart_amont(request)}, status=200)

                except Cart.DoesNotExist:
                    return JsonResponse({'status': 'failed', 'message': 'you dont have item in this cart'}, status=400)

            except Fooditem.DoesNotExist:
                return JsonResponse({'status': 'failed', 'message': 'invalid-request'}, status=400)
            
       

    else:
        return JsonResponse({'status': 'login_required', 'message': 'you need to login first'}, status=401)
    
    
    
    
@login_required(login_url='login', redirect_field_name='login')

def cart(request):    
    
    
    if request.user.is_authenticated:
        cart_item=Cart.objects.filter(user=request.user).order_by('created_at')
        # Nothing but the it of the 2 fooditem 
        
    else:
        cart_item=None
    
    context={
        'cart_item':cart_item,
    }
    print(context)
    
    return render(request,'market/cart.html',context)


def delete_cart(request,cart_id):
    
    if request.user.is_authenticated:
        try:
            cart_item=Cart.objects.filter(user=request.user,id=cart_id) 
            print(cart_item)
         

            try:
                if cart_item:
                    cart_item.delete()
                    return JsonResponse({'status':'success','message':'delete successfully','cart_counter':get_cart_counter(request),'cart_amount':get_cart_amont(request)})
                else:
                    return JsonResponse({'status':'error','message':'you cant delete'})  
                
            except:
                return JsonResponse({'status':'success','message':'cart item doesnot exit'})

                
                
            return JsonResponse({'status':'success','message':'cart item fetch successfully'})

        except:
            return JsonResponse({'status':'error','message':'cart_item error'})
    
    
    
    else:
        return JsonResponse({'status': 'login_required', 'message': 'you need to login first'}, status=401)
    
    
    
    
    
def search(request):
    add=request.GET.get('address')
    lat=request.GET.get('lat')
    lan=request.GET.get('lan')
    radius=request.GET.get('radius')
    keyword=request.GET.get('keyword')
    
    
    
    # This functionality is good but it is not a smart way to handle the search functinality 
    # so we need to make the search function available for foodname
    
    
    
    fetch_vendor_by_fooditem=Fooditem.objects.filter(foodtitle__icontains=keyword,is_avalable=True).values_list('vendor')
    print(fetch_vendor_by_fooditem)
    
    vendor=Vendor.objects.filter(Q(id__in=fetch_vendor_by_fooditem) | Q(vendor_name__icontains=keyword,is_approved=True,user__is_active=True))
    vendor_count=vendor.count()
    context={
        'vendor':vendor,
        'vendor_count':vendor_count
        
        
    }
       
   
    return render(request,'market/listing.html',context)