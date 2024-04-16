from django.shortcuts import render,HttpResponse

from accounts.forms import Userform
from accounts.forms import Userprofile_form,Userinfoform
from django.shortcuts import get_object_or_404  # Import get_object_or_404
from accounts.models import Userprofile
from django.contrib import messages
from django.shortcuts import redirect
from accounts.context_processor import get_profile


# Create your views here.
def customerprofile(request):
    user_profile =get_object_or_404(Userprofile,user=request.user)
    # print(user_profile,'here is customer profile')

    if request.method == 'POST':
        userprofile_form = Userprofile_form(request.POST, request.FILES, instance=user_profile)
        userinfoform = Userinfoform(request.POST, request.FILES,instance=request.user)

        if userprofile_form.is_valid() and userinfoform.is_valid():
            try:
                userprofile_form.save()
                userinfoform.save()
                # print(request.user,'which user  is this ')
                messages.success(request,'profile got updated')

                return redirect('customerprofile')
            except Exception as e:
                return HttpResponse(e)
    else:
        userprofile_form = Userprofile_form()
        userinfoform = Userinfoform()

    context = {
        'Userinfoform': userinfoform,
        'userprofile_form': userprofile_form,
        'get_profile':get_profile
        
    }

    return render(request, 'customer/customerprofile.html', context)