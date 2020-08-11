from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("CustomFields", {'fields': ('avatar', "gender", "bio", "birthdate",
                                        "language", "currency", "superhost")}),)

    list_display = ("username", "first_name", "last_name", "email", "is_active", "language", "currency",
                    "is_staff", "is_superuser",)

    list_filter = UserAdmin.list_filter + ("superhost",)