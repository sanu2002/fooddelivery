from.models import Custom_User

def detect(user):
    if user is not None:
        if user.role == Custom_User.VENDOR:
            redirecturl = 'vendashboard'
        elif user.role == Custom_User.CUSTOMER:
            redirecturl = 'customerdashboard'
        elif user.role is None and user.is_superuser:
            redirecturl = '/login'
        return redirecturl



from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMessage
from foodonlineproject import settings
from django.contrib.auth.tokens import default_token_generator



def send_verification_email(request,user,mail_subject,email_template):
    current_site=get_current_site(request)
    message=render_to_string(email_template,{
        'user':user,
        'domain':current_site,
        'uid':urlsafe_base64_encode(str(user.pk).encode('utf-8')),
        'token':default_token_generator.make_token(user)
     })
 

    from_email = settings.EMAIL_HOST_USER
    to=user.email
    msg = EmailMessage(mail_subject,message,from_email,[to])
    
    msg.send()
    
    
    
from django.core.mail import send_mail





# testing email 
    
# from django.core.mail import send_mail
# from django.conf import settings

# def send(request):
#     subject = 'Auto Generated Message'
#     message = 'I am your uncle'
#     from_email = settings.EMAIL_HOST_USER
#     to = 'sanujitmajhi473@gmail.com'  # To send to multiple recipients, use a list.

#     res=send_mail(subject, message, from_email, [to])
    
#     return res


# we want to optimise the code and send the  subject dynamically 


# def send_password_reset_email(request,user):
    
#     current_site=get_current_site(request)
#     mail_subject='Reset your password'
#     message=render_to_string('accounts/emails/reset_password_email.html',{
#         'user':user,
#         'domain':current_site,
#         'uid':urlsafe_base64_encode(str(user.pk).encode('utf-8')),
#         'token':default_token_generator.make_token(user)
#      })
 

#     from_email = settings.EMAIL_HOST_USER
#     to=user.email
#     msg = EmailMessage(mail_subject,message,from_email,[to])
    
#     msg.send()
    
    
