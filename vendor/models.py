from django.db import models

# Create your models here.
from accounts.models import Custom_User,Userprofile
from  .utils import send_notification

class Vendor(models.Model):
    user=models.OneToOneField(Custom_User,on_delete=models.CASCADE)
    user_profile=models.OneToOneField(Userprofile,related_name='userprofile',on_delete=models.CharField)
    vendor_name=models.CharField(max_length=50)
    vendor_license=models.ImageField(upload_to='vendor/license')
    is_approved=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.vendor_name
    
    # so the reason why i am targettting this save functioin is just because behind 
    # the scene wen i cahnge the is_approved button from the admin pannel then there is 
    # something happend with save buttton so instaed of thinking more i jump into save 
    # button and try to handle the save button functionality 
    
    
    def save(self, *args, **kwargs):
        if self.pk is not None:
            instance = Vendor.objects.get(pk=self.pk)
            if instance.is_approved != self.is_approved:
                mail_template = 'accounts/emails/adminsapprov.html'
                context = {
                    'user': self.user,
                    'is_approved': self.is_approved,
                }
                
                if self.is_approved:
                    mail_subject = 'Congratulations, your restaurant has been approved'
                else:
                    mail_subject = 'We are sorry, you are not eligible for this'
                
                send_notification(mail_subject, mail_template, context)

        super(Vendor, self).save(*args, **kwargs)