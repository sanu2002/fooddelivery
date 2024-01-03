from django.db import models

from accounts.models import Custom_User

from menuapp.models import Fooditem


# Create your models here.

class Cart(models.Model):
    user=models.ForeignKey(Custom_User,on_delete=models.CASCADE)
    fooditem=models.ForeignKey(Fooditem,on_delete=models.CASCADE)
    quantitiy=models.PositiveIntegerField()
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    def __unicode__(self):
        return self.user 