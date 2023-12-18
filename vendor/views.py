from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import Vendorform
from .models import Vendor
from accounts.forms import Userprofile_form
from accounts.models import Userprofile
from django.db import IntegrityError
from django.http import JsonResponse
from .utils import *

from menuapp.models import Fooditem


import json
from django.utils.text import slugify

from .forms import *
# logger = logging.getLogger(__name__)
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.decorators import login_required




@login_required(redirect_field_name='login')
def vprofile(request):
    profile_instance = get_object_or_404(Userprofile, user=request.user)
    vendor_instance = get_object_or_404(Vendor, user=request.user)

    if request.method == 'POST':
        profile_form = Userprofile_form(request.POST, request.FILES, instance=profile_instance)
        vendor_form = Vendorform(request.POST, request.FILES, instance=vendor_instance)

        if profile_form.is_valid() and vendor_form.is_valid():
            profile_form.save()
            vendor_form.save()
            messages.success(request, 'Settings updated')
            return redirect('vprofile')
        else:
            print(profile_form.errors)
            print(profile_form.errors)
    else:
        profile_form = Userprofile_form(instance=profile_instance)
        vendor_form = Vendorform(instance=vendor_instance)

    context = {
        'profile_form': profile_form,
        'vendor_form': vendor_form,
        'profile_instance': profile_instance,
        'vendor_instance': vendor_instance
    }

    return render(request, 'vendor/v_profile.html', context)
# def vendor_update(request):
# or else you can write within that vprofile 

    # print(request)
    # if request.method == 'POST':
    #     profile_instance=get_object_or_404(Userprofile,user=request.user)
    #     vendor_instance=get_object_or_404(Vendor,user=request.user)
    
    #     userprofile_form = Userprofile_form(request.POST,request.FILES,instance=profile_instance)
    #     vendor_form = Vendorform(request.POST,request.FILES,instance=vendor_instance)
        
        
    #     if userprofile_form.is_valid() and vendor_form.is_valid():
    #         vendor_license = vendor_form.cleaned_data['vendor_license']
    #         vendor_name = vendor_form.cleaned_data['vendor_name']
    #         profile_picture = userprofile_form.cleaned_data['profile_pictutre']
    #         cover_photo = userprofile_form.cleaned_data['cover_photo']
    #         addressline_1 = userprofile_form.cleaned_data['addressline_1']
    #         addressline_2 = userprofile_form.cleaned_data['addressline_2']
    #         city = userprofile_form.cleaned_data['city']
    #         state = userprofile_form.cleaned_data['state']
    #         pincode = userprofile_form.cleaned_data['pincode']
    #         longtitude = userprofile_form.cleaned_data['longtitude']
    #         latitude = userprofile_form.cleaned_data['latitude']

    #         user_profile_instance = userprofile_form.save()
    #         vendor_instance = vendor_form.save()
            
    #         print('Userprofile instance executed:', user_profile_instance)
    #         print('Vendor instance executed:', vendor_instance)
            
    #         return redirect('vprofile')
    #     else:
    #         print("Form validation failed")
    #         print("Userprofile errors:", userprofile_form.errors)
    #         print("Vendor details errors:", vendor_form.errors)
    
    # return HttpResponse('successfully updated')
    

    
    
import logging

def menu_builder(request):
    vendor=Vendor.objects.all()
    category=Category.objects.filter(vendor__in=vendor)
    print(category)
    context={'category':category}
    
    return render(request,'vendor/menu_builder.html',context)
  




def add_category(request):
    if request.method == 'POST':
        catform = Category_form(request.POST)
    
        if catform.is_valid():
            category_name = catform.cleaned_data['category_name']
            slug = slugify(category_name)  # Generate the slug
            description = catform.cleaned_data['description']

            # Update the cleaned_data dictionary with the generated slug
            catform.cleaned_data['slug'] = slug

            # Create and save the Category object
            category = Category(category_name=category_name, slug=slug, description=description, vendor=request.user.vendor)
            category.save()
            
            messages.success(request, 'New category added successfully in the database')
            return redirect('menu_builder')
    
    else:
        catform = Category_form()

    context = {'catform': catform}
    return render(request, 'vendor/add_cat.html', context)



def cat_update(request, pk):
    cat = Category.objects.get(pk=pk)

    if request.method == 'POST':
        cat_update_form = Category_form(request.POST, request.FILES, instance=cat)

        if cat_update_form.is_valid():
            # Update only the fields that are provided in the form
            category_name=cat_update_form.cleaned_data['category_name']
            category=cat_update_form.save(commit=False)
            category.vendor=get_vendor(request)
            category.slug=slugify(category_name)
            cat_update_form.save()
            messages.success(request,'Your category update successfully')
            return redirect('menu_builder')
            
            
                        

        else:
            print(cat_update_form.errors)
    else:
        cat_update_form = Category_form(instance=cat)

    context = {
        'cat_update_form': cat_update_form,
    }

    return render(request, 'vendor/update_cate.html', context)

def cat_delete(request,pk):
    
    instance=get_object_or_404(Category,pk=pk)
    instance.delete()
    return redirect('menu_builder')
    





def addfood_bycat(request,pk=None):
    vendor=Vendor.objects.get(user=request.user)
    category=get_object_or_404(Category,pk=pk)
    fooditem=Fooditem.objects.filter(vendor=vendor,category=category)
    context={
        'fooditem':fooditem,
        'category':category
    }
    
    
    
  
    return render(request,'vendor/add_food.html',context)



def food_delete(request,id):
    instance=get_object_or_404(Fooditem,id=id)

    if instance:
        instance.delete()
        return redirect('menu_builder')
    else:
        return redirect('menu_builder')
    


def add_food(request):
    food_form = Food_form()  # Initialize the form outside the conditional block
    
    if request.method == 'POST':
        food_form = Food_form(request.POST, request.FILES)
        vendor = get_vendor(request)
        
        if food_form.is_valid():
            food_item = food_form.save(commit=False)  # Save the form data to a model instance without committing to the database
            food_item.vendor = vendor  # Set the vendor before saving
            food_item.save()  # Save the modified instance to the database
            return redirect('menu_builder')
        else:
            print(food_form.errors)
   
    context = {
        'food_form': food_form,
    }

    return render(request, 'vendor/addfoodform.html', context)



def food_update(request, pk):
    food = get_object_or_404(Fooditem, pk=pk)

    if request.method == 'POST':
        form = Food_form(request.POST, request.FILES, instance=food)
        if form.is_valid():
            foodtitle = form.cleaned_data['foodtitle']
            food = form.save(commit=False)
            food.vendor = get_vendor(request)
            food.slug = slugify(foodtitle)
            form.save()
            messages.success(request, 'Food item updated successfully')
            return redirect('addfood_bycat',food.category.id)
        else:
            print(form.errors)
            
    else:
        form = Food_form(instance=food)

    context = {
        'form': form,
        'food': food
    }

    return render(request, 'vendor/food_upadte.html', context)



