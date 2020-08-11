from django.contrib import admin
from .models import *

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("__str__", "rating_average", )