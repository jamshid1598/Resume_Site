from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE

from .models import UserInfo

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display=[
        'user_name', 
        'user_profession', 
        'user_phone', 
        'user_email', 
        'user_address', 
        'facebook_link', 
        'instagram_link', 
        'telegram_link', 
        'whatsup_link', 
        'linkedin_link', 
        'github_link', 
        'stackoverflow_link', 
        'facebook_link', 
    ]
    search_fields=[
        'user_name', 
        'user_profession', 
        'user_phone', 
        'user_email', 
        'user_address', 
        'facebook_link', 
        'instagram_link', 
        'telegram_link', 
        'whatsup_link', 
        'linkedin_link', 
        'github_link', 
        'stackoverflow_link', 
        'facebook_link', 
    ]
    list_display_links=[
        'user_name', 
        # 'user_profession', 
        # 'user_phone', 
        # 'user_email', 
        # 'user_address', 
        'facebook_link', 
        'instagram_link', 
        'telegram_link', 
        'whatsup_link', 
        'linkedin_link', 
        'github_link', 
        'stackoverflow_link', 
        'facebook_link', 
    ]
    list_editable = [
        # 'user_name', 
        'user_profession', 
        'user_phone', 
        'user_email', 
        'user_address', 
        # 'facebook_link', 
        # 'instagram_link', 
        # 'telegram_link', 
        # 'whatsup_link', 
        # 'linkedin_link', 
        # 'github_link', 
        # 'stackoverflow_link', 
        # 'facebook_link', 
    ]

    fieldsets=(
        ('Basic Info', {'fields' : [
                            'user_image',    
                            'user_name', 
                            'user_profession', 
                ],
            },
        ),
        (
            'Contact Info', {
                'fields': [
                    'user_phone', 
                    'user_email', 
                    'user_address', 
                ],
            },
        ),
        (
            'Social Links', {
                'fields': [
                    'facebook_link', 
                    'instagram_link', 
                    'telegram_link', 
                    'whatsup_link', 
                    'linkedin_link', 
                    'github_link', 
                    'stackoverflow_link', 
                ],
            },
        ),
        (
            'Core Info', {
                'fields' :[
                    'user_info',
                    'user_experience',
                    'user_edu',
                ],
            },
        ),
    )
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }
admin.site.register(UserInfo, UserInfoAdmin)