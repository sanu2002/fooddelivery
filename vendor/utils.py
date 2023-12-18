
    
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMessage
from foodonlineproject import settings
from django.contrib.auth.tokens import default_token_generator    



from django.conf import settings

def send_notification(mail_subject, mail_template, context):
    from_email = settings.EMAIL_HOST_USER
    message = render_to_string(mail_template, context)
    to_email = context['user'].email
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.send()
    
    
    
def get_vendor(request):
    if request.user.is_authenticated:
        return request.user.vendor
    else:
        return None