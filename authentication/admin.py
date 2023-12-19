from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add a list_display to see more fields in the admin interface
    list_display = ['username', 'first_name', 'last_name', 'email', 'gender', 'is_staff', ]

admin.site.register(CustomUser)