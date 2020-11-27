from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.




class UserInfo(models.Model):
    user_image      = models.ImageField(upload_to='user image/%Y/%m/%d/', verbose_name='User Image')
    user_name       = models.CharField(max_length=200)
    user_profession = models.CharField(max_length=500)
    
    # contact info
    user_phone     = PhoneNumberField()
    user_email     = models.EmailField(blank=True, null=True)
    user_address   = models.CharField(max_length=500)

    # social network info
    facebook_link       = models.CharField(max_length=200, blank=True, null=True)
    instagram_link      = models.CharField(max_length=200, blank=True, null=True)
    telegram_link       = models.CharField(max_length=200, blank=True, null=True)
    whatsup_link        = models.CharField(max_length=200, blank=True, null=True)
    linkedin_link       = models.CharField(max_length=200, blank=True, null=True)
    github_link         = models.CharField(max_length=200, blank=True, null=True)
    stackoverflow_link  = models.CharField(max_length=200, blank=True, null=True)
    # facebook_link  = models.CharField(max_length=200, blank=True, null=True) 

    # specialist info about user 
    user_info       = models.TextField(verbose_name='About Me')
    user_experience = models.TextField(verbose_name='Experience')
    user_edu        = models.TextField(verbose_name='Education And Training')

    def __str__(self):
        return self.user_name
