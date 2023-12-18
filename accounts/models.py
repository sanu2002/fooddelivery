from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError('You should give an email')
        if not username:
            raise ValueError('You should provide a proper name')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        email = self.normalize_email(email)
        user = self.create_user(email, username, first_name, last_name, password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Custom_User(AbstractBaseUser, PermissionsMixin):
    VENDOR = 1
    CUSTOMER = 2
    ROLE_CHOICES = (
        (VENDOR, 'RESTAURANT'),
        (CUSTOMER, 'CUSTOMER')
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_role(self):
        user_role = ''
        if self.role == self.VENDOR:
            user_role = 'RESTAURANT'
        elif self.role == self.CUSTOMER:
            user_role = 'CUSTOMER'
        return user_role


class Userprofile(models.Model):
    user = models.OneToOneField('Custom_User', on_delete=models.CASCADE)
    profile_pictutre=models.ImageField(upload_to='user/profile_pictures',blank=True,null=True)
    cover_photo=models.ImageField(upload_to='user/cover_pictures',blank=True,null=True)
    addressline_1=models.CharField(max_length=50,blank=True,null=True)
    addressline_2=models.CharField(max_length=50,blank=True,null=True)
    city=models.CharField(max_length=15,blank=True,null=True)
    state=models.CharField(max_length=15,blank=True,null=True)
    pincode=models.CharField(max_length=20,null=True,blank=True)
    longtitude=models.CharField(max_length=20,null=True,blank=True)
    latitude=models.CharField(max_length=20,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.email
    
    def full_address(self):
        return f"{self.addressline_1},{self.addressline_2}"
    


@receiver(post_save, sender=Custom_User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Userprofile.objects.create(user=instance)
        print('User profile created')
    else:
        try:
            user_profile = Userprofile.objects.get(user=instance)
            # Update user_profile fields here if needed
            user_profile.save()
            print('User profile updated successfully')
        except Userprofile.DoesNotExist:
            Userprofile.objects.create(user=instance)
            print('User profile created because it was not available before')



# post_save.connect(post_save_create_profile_receiver,sender=Custom_User)

# use this decorator instead of manually write the code 



