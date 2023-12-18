from django.db import models
from vendor.models import Vendor


# Create your models here.

class Category(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50, unique=True, default='DefaultCategoryName')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.category_name

    
class Fooditem(models.Model):
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    foodtitle=models.CharField(max_length=50)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=250,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    is_avalable=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='foodimages')
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.foodtitle

                                                        