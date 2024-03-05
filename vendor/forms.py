from typing import Any
from django import forms 
from accounts.custom_validation import  valid_file
from menuapp.models import *

from accounts.context_processor import get_vendor

from .models import Openinghour

from.models import Vendor
class Vendorform(forms.ModelForm):
    vendor_license=forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info'}),validators=[valid_file])

    class Meta:
        model = Vendor
        fields =['vendor_name','vendor_license']
        
    # def customise_save_vendor(self,commit=True):
    #     user=super(Vendor,self).save(commit=False)
        
    #     if commit:
    #         vendor_update(self)
    #         user.save()
            
    #     return user
            


class  Category_form(forms.ModelForm):
    category_name=forms.CharField(max_length=200,required=False)
    description=forms.CharField(max_length=200,required=False)
    
    
    class Meta:
        model=Category
        fields=['category_name','description',]
        
    def clean(self):
        cleaned_data = super().clean()

        # Check if all fields are empty
        if not cleaned_data['category_name']:
            raise forms.ValidationError("Category name cannot be empty.")

        return cleaned_data

        
class Food_form(forms.ModelForm):
    class Meta:
        model=Fooditem
        fields=['category','foodtitle','slug','description','price','is_avalable','image']

# foodtittle
# slug 
# descrioption 
# price
# is_avalable
# image
# and i will create the vendor instance and category object 
# and save it(for vendor we no need to care about  but for making 
# food we need to create the object)
       
class Openinghourform(forms.ModelForm):
      class Meta:
            model=Openinghour
            fields=['day','from_hour','to_hour','is_closed']
            
            
            
     
        
