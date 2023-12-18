from django.shortcuts import render

# Create your views here.

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