from django.contrib import admin

from vendor.models import Vendor,Openinghour

# Register your models here.
class Vendoradmin(admin.ModelAdmin):
    list_display=['user','vendor_name','is_approved','created_at']
    list_display_links=['user','vendor_name']
    list_editable=['is_approved']
    
    
class Openinghouradmin(admin.ModelAdmin):
      list_display=('vendor','day','from_hour','to_hour','is_closed')
      
    
    

admin.site.register(Vendor,Vendoradmin)
admin.site.register(Openinghour,Openinghouradmin)