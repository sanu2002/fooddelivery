from django.contrib import admin

# Register your models here.
from .models import *

class Cart_admin(admin.ModelAdmin):
    list_display=['user','fooditem','quantitiy','created_at','updated_at']



admin.site.register(Cart,Cart_admin)

    


