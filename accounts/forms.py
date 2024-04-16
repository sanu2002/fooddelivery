from django import forms

from .models import Custom_User,Userprofile
from django.shortcuts import render
from .custom_validation import valid_file




class Userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model=Custom_User
        fields=['first_name','last_name','username','email','password','confirm_password']
        
        
    def clean(self):
        clean_data=super(Userform,self).clean()
        password=clean_data.get('password')
        confirm_password=clean_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('password Does not match')
          
          
class Userprofile_form(forms.ModelForm):
    profile_pictutre=forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info'}),validators=[valid_file])
    cover_photo=forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info'}),validators=[valid_file])
    
    longtitude=forms.FloatField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    latitude=forms.FloatField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    
    # there is an alternate method avalable by iteratine the fields 
    
    # addressline_1 = forms.CharField(widget=forms.TextInput(attrs={'id': 'ipaddress'}), max_length=50)
    # customization needed otherwise wen you aplied the autocomplete the it will take 
    # id_adreesline1 by default 

    
    class Meta:
        model = Userprofile
        fields=['profile_pictutre','cover_photo','addressline_1','addressline_2','city','state','pincode',
              'longtitude','latitude', ]
        
        
    # in the big project it is best 
    # def __init__(self,*args,**kwargs):
    #     super(Userprofile_form,self).__init__(*args)
        
    #     for field in self.fields:
    #         if  field=='longtitude' or field=='latitude':
    #               self.fields[field].widget.attrs['readonly']='readonly'
        
        
        
    # def user_profile_save(self,commit=True):
    #     user=super(Userprofile_form,self).save(commit=False)
    #     if commit:
    #         vendor_update(self)
    #         user.save() 
            
    #     return user
   
class Userinfoform(forms.ModelForm):
    class Meta:
        model=Custom_User
        fields=['first_name', 'last_name', 'phone_number']
    