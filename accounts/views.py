from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .forms import Userform
from vendor.forms import Vendorform

from django.template.defaultfilters import slugify

from django.contrib.auth import authenticate
from vendor.models import Vendor

from django.contrib import messages,auth

from .models import Custom_User,Userprofile
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
from accounts.utils import detect

from.utils import send_verification_email



from foodonlineproject import settings


from django.core.mail import send_mail






def check_vendorrole(user):
    try:
     if user.role==1:
        return True
    
    except Exception as e:
        raise e
        


def check_customer(user):
    try:
        if user.role==2:
            return True
        
        
    except Exception as e:
        raise e
        

from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator    
from django.utils.encoding import force_str, force_bytes


def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Custom_User.objects.get(pk=uid)

        if default_token_generator.check_token(user, token):
            # Mark the user as active
            user.is_active = True
            user.save()
            return HttpResponse('Your email has been successfully validated.')
        else:
            return HttpResponse('Invalid validation link. Please request a new one.')
    except (TypeError, ValueError, OverflowError, Custom_User.DoesNotExist):
        return HttpResponse('Invalid validation link.')

    return HttpResponse('Validation failed.')
  







def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already loggged in')
        return redirect('dashboard')
    
    
    elif request.method == 'POST':
            form=Userform(request.POST)
             # here the details will save in user field but role not given automatically so we need to halt this
            #  another problem we are storing the password in a plane tect format we need to hash them before saving into the database 
             
            #  create the user using form 
            if form.is_valid():
            #      password=form.cleaned_data['password']
            #      user=form.save(commit=False)
            #      user.set_password(password)
            #      user.role=Custom_User.CUSTOMER
            #      user.save()
            
            #  crate the user using create_user
            
                first_name=form.cleaned_data['first_name']
                last_name=form.cleaned_data['last_name']
                email=form.cleaned_data['email']
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                
                user=Custom_User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                user.role=Custom_User.CUSTOMER
                user.save()
                
                mail_subject='Validate your email'
                email_template='accounts/emails/account_verification_email.html'
                send_verification_email(request,user,mail_subject,email_template)
                # send email verfication before redirect to the url page 
                # send_verification_email=(request,user)
                # code the logic in the utils file 
                
                
                
                messages.success(request,'You Have succeefully Registerd plese vaerfy your email')
                # messages.error(request,'You Have succeefully Registerd')
                
                # Ok if i receive some error then how my html pafe determine that whic type of error i ma receiving so
                # you have to do little bit configuration in setting 
                # after do some settins you will get the appropriate css color 
                
                return redirect('registerUser')
            else:          
                print('invalid form')

                print(form.errors)
                
        # after that you have to focus on fields error and non-fields error fields erroe like username and etc
        # and non-field error like confirm password 

            
             
               
    else:
        form=Userform()


    context={
                        'forms':form,
                    }
             
        

   
    return render(request,'accounts/registerUser.html',context)



def registerVendor(request):
    if request.user.is_authenticated:
        messages.success(request,'you are already a logged-in user')

        return redirect('myaccount')
       
    
    
    
    elif request.method=='POST':
            form=Userform(request.POST)
            v_form=Vendorform(request.POST,request.FILES)
            
            if form.is_valid() and v_form.is_valid():
                first_name=form.cleaned_data['first_name']
                last_name=form.cleaned_data['last_name']
                email=form.cleaned_data['email']
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                
                
                user=Custom_User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                user.role=Custom_User.VENDOR
                user.save()
                
                vendor=v_form.save(commit=False)
                print(vendor,'here is the vendor data wen vendor got created')
                vendor.user=user 
                vendor_name=v_form.cleaned_data['vendor_name']
                vendor.vendor_slug = slugify(vendor_name) + '-' + str(user.id)
                user_profile=Userprofile.objects.get(user=user)
                vendor.user_profile=user_profile
                print('i am here')
                
                vendor.save()
                messages.success(request,'YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY PLEASE WAIT FOR APPROVAL')
                return redirect('registerVendor')
                
                
                
            else:
                print(form.errors)            
    else:
        form=Userform()
        v_form=Vendorform()
        
    
    
    form=Userform()
    v_form=Vendorform()
    
    context={
        'forms':form ,
        'v_form':v_form
        
    }
    
    
    return render(request,'accounts/registerVendor.html',context)



def login(request):
    if request.user.is_authenticated:
        return redirect('myaccount')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            user = auth.authenticate(request, email=email, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('myaccount')
            else:
                messages.error(request, 'Invalid sign in')
        else:
            messages.error(request, 'Please provide both email and password')

    return render(request, 'accounts/login.html')

# //this will prevent user for directly access to any url 
# field that you need to show  to the  user after login/register so
# that  is beneficla for that time 


def logout(request):
    auth.logout(request)
    messages.info(request,'You are successfully loged out')
    return redirect('login')


        

# ___________________________________________________



# In our flow chart we have complted the half of the project next is to 
# detect the user and vendor then after that redirect to its appropriate dashboard 


# vendordashborad
# customerdashborad
# get the role from models custom user by making method of that class





@login_required(redirect_field_name='login')
def myaccount(request):
    # now here i am not gomma right the logic here i will crate a helper file 
    # utils.py and use that url for redirect
    user=request.user
    redirecturl=detect(user)
  
    return redirect(redirecturl)


def check_vendorrole(user):
    return user is not None and (user.role == 1)

def check_customer(user):
    return user is not None and (user.role == 2)

# if you are using lambda function then no need to write this abov 2 line


@login_required(redirect_field_name='login')
# @user_passes_test(lambda user: detect(user) == 'vendashboard')
@user_passes_test(check_vendorrole)
def vendashboard(request):

    
    return render(request, 'accounts/vendashboard.html')

@login_required(redirect_field_name='login')
# @user_passes_test(lambda user: detect(user) == 'customerdashboard')




@user_passes_test(check_customer)
def customerdashboard(request):
    return render(request, 'accounts/customerdashboard.html')








def forgetpassword(request):
    if request.method=='POST':
        email = request.POST.get('email')  # Use request.POST.get to avoid a potential KeyError

        try:
            user = Custom_User.objects.get(email=email)  # Use 'objects' manager to get the user
            
            # we are setting this because we want to overide the details only the content change dynamicaslly 
            mail_subject='Reset your password'
            email_template='accounts/emails/reset_password_email.html'
            send_verification_email(request, user,mail_subject,email_template)
            messages.success(request, 'Reset link successfully sent')
        except Custom_User.DoesNotExist:
            messages.error(request, 'User with this email does not exist')

                
    
    return render(request,'accounts/forget_password.html')
        
        
def resetpassword_validate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Custom_User.objects.get(pk=uid)
        
    except Exception as e:
        user=None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid']=uid
        messages.info(request,'plese reset your password')
        return redirect('resetpassword')
        
    else:
        messages.error(request,'This link has been expired')
        return redirect('myaccount')
        
    


def resetpassword(request):
    if request.method=='POST':
        password=request.POST['PASS1']
        confirm_password=request.POST['CPASS']
        if password==confirm_password:
            pk=request.session.get('uid')
            user=Custom_User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active=True
            user.save()
            messages.success(request,'Password reset successful')
            return redirect('login')
        else:
            messages.error(request,'password doesnot match')
            return redirect('resetpassword')
        
    return render(request,'accounts/reset_password.html')

    
# now i will add the vendor functionality like token verification and admin approval 



