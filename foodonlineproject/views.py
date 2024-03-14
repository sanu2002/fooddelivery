import googlemaps
import json
from foodonlineproject import settings
from django.shortcuts import render, redirect

from accounts.context_processor import get_vendor

from accounts.models import Userprofile
from vendor.models import Vendor

from django.shortcuts import render

def index(request):
    # vendor=get_vendor(request)This is not applicable why just because i need all the restaurant details 
    vendor=Vendor.objects.all()
    context={
        'vendors':vendor
    }
    return render(request,'home.html',context)


# def geocode1(request):
    # clubs = Userprofile.objects.all()
    # context = {
    #     'clubs':clubs,
    # }
    # return render(request, 'geocode.html',context)




# def geoocode(request, pk):
    adress = Userprofile.objects.get(id=pk)
    
    if adress.latitude and adress.longtitude and adress.city is not None:
        my_string = f"{adress.latitude},{adress.longtitude},{adress.city}"
        
        # Geocode the string
        gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEYS)
        result = gmaps.geocode(my_string)

        if result:
            latitude = result[0]['geometry']['location']['lat']
            longtitude = result[0]['geometry']['location']['lng']
            
            adress.latitude = latitude
            adress.longtitude = longtitude
            adress.save()
        else:
            # Handle the case where geocoding fails
            pass

    else:
        # Handle the case where latitude, longitude, or city is missing
        pass

    context = {
        'result': json.dumps(result),
        'latitude': latitude if result else None,
        'longitude': longtitude if result else None
    }

    return render(request, 'geocode.html', context)


