from django import forms
from django.forms import formset_factory
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber

from .models import UserInfo

class UserInfoModelForm(forms.ModelForm):

    user_image = forms.ImageField(label='Image:')
    user_name = forms.CharField(max_length=200, label="Full Name:")
    user_profession = forms.CharField(max_length=500, label="Profession:")
    
    # user_phone = PhoneNumber.from_string(phone_number=raw_phone, region='UZB').as_e164
    user_phone = PhoneNumberField(label="Phone Number:")
    user_email = forms.EmailField(label="Email:")
    user_address = forms.CharField(max_length=500, label="Address:")
    
    facebook_link = forms.CharField(max_length=200, required=False, label="Facebook:")
    instagram_link = forms.CharField(max_length=200, required=False, label="Instagram:")
    telegram_link = forms.CharField(max_length=200, required=False, label="Telegram:")
    whatsup_link = forms.CharField(max_length=200, required=False, label="What's up:")
    linkedin_link = forms.CharField(max_length=200, required=False, label="Linked In:")
    github_link = forms.CharField(max_length=200, required=False, label="GitHub:")
    stackoverflow_link = forms.CharField(max_length=200, required=False, label="Stack Overflow:")
    # facebook_link = forms.CharField(max_length=200, required=False)
    
    user_info = forms.CharField(widget = forms.Textarea(), label="About Me:") 
    user_experience = forms.CharField(widget = forms.Textarea(), label="Experiance:")
    user_edu = forms.CharField(widget = forms.Textarea(), label="Education and Training:")

    class Meta:
        model = UserInfo
        fields = ('user_image', 'user_name', 'user_profession', 
        'user_phone', 'user_email', 'user_address', 
        
        'facebook_link', 'instagram_link', 'telegram_link', 'whatsup_link', 
        'linkedin_link', 'github_link', 'stackoverflow_link', 
        
        'user_info', 'user_experience', 'user_edu')


class UserInfoForm(forms.Form):

    user_image = forms.ImageField(label='Image:')
    user_name = forms.CharField(max_length=200, label="Full Name:")
    user_profession = forms.CharField(max_length=500, label="Profession:")
    
    # user_phone = PhoneNumber.from_string(phone_number=raw_phone, region='UZB').as_e164
    user_phone = PhoneNumberField(label="Phone Number:")
    user_email = forms.EmailField(label="Email:")
    user_address = forms.CharField(max_length=500, label="Address:")
    
    facebook_link = forms.CharField(max_length=200, required=False, label="Facebook:")
    instagram_link = forms.CharField(max_length=200, required=False, label="Instagram:")
    telegram_link = forms.CharField(max_length=200, required=False, label="Telegram:")
    whatsup_link = forms.CharField(max_length=200, required=False, label="What's up:")
    linkedin_link = forms.CharField(max_length=200, required=False, label="Linked In:")
    github_link = forms.CharField(max_length=200, required=False, label="GitHub:")
    stackoverflow_link = forms.CharField(max_length=200, required=False, label="Stack Overflow:")
    # facebook_link = forms.CharField(max_length=200, required=False)
    
    user_info = forms.CharField(widget = forms.Textarea(), label="About Me:") 
    user_experience = forms.CharField(widget = forms.Textarea(), label="Experiance:")
    user_edu = forms.CharField(widget = forms.Textarea(), label="Education and Training:")

    class Meta:
        model = UserInfo
        fields = ('user_image', 'user_name', 'user_profession', 
        'user_phone', 'user_email', 'user_address', 
        
        'facebook_link', 'instagram_link', 'telegram_link', 'whatsup_link', 
        'linkedin_link', 'github_link', 'stackoverflow_link', 
        
        'user_info', 'user_experience', 'user_edu')

UserInfoFormSet = formset_factory(UserInfoForm, extra=3)