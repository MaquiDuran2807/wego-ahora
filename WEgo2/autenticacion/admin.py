from django.contrib import admin

# Register your models here.

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass