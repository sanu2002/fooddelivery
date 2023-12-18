from vendor.models import Vendor

def get_vendor(request):
    try: 
      vendor=Vendor.objects.get(user=request.user) 
      
    except:
        vendor=None
        
    return dict(vendor=vendor)
   
    # try:
    #     vendor = Vendor.objects.get(user=request.user)
    # except Vendor.DoesNotExist:
    #     # Handle the case where the vendor does not exist
    #     vendor = None

    # context = {
    #     'vendor': vendor,
    # }
    
    # no need to write this code on views
    
from foodonlineproject import settings
    
def get_google_api(request):
  return {'Googleapi':settings.GOOGLE_API_KEYS}