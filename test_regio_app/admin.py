from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_filter = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name', 'iban']

admin.site.register(UserProfile, UserProfileAdmin)