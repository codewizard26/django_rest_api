from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager

class CustomUser(AbstractBaseUser):

    def has_perms(self, perm, obj=UserManager):
        return self.is_superuser

    def has_perm(self, perm, obj=UserManager):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
        
    name = models.CharField(max_length=50,default="anonymous")
    email = models.EmailField(max_length=50,unique=True)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []
# Create your models here.

    phone= models.CharField(max_length=10,blank=True,null = True)
    gender=models.CharField(max_length=10,blank = True,null= True)

  
    session_token = models.CharField(max_length=10,default=0)
   
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(null= True)
    is_superuser = models.BooleanField(null = True)

    objects = UserManager()