from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ["username", "email", "first_name", "age", "is_staff"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age", "bio")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("first_name", "email", "age")}),)
