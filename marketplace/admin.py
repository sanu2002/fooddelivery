from django.contrib import admin

# Register your models here.
from .models import *

class Cart_admin(admin.ModelAdmin):
    list_display=['user','fooditem','quantitiy','created_at','updated_at']

class Tax_admin(admin.ModelAdmin):
    list_display=['tax_type','tax_percentage','is_active']


admin.site.register(Cart,Cart_admin)
admin.site.register(Tax,Tax_admin)

    


