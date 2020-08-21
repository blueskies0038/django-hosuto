from django.contrib import admin
from .models import *

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("room", "check_in", "check_out", "guest", "in_progress", "is_finished")

    lsit_filter = ("status")

@admin.register(BookedDay)
class BookedDayAdmin(admin.ModelAdmin):
    list_display = ("day", "reservation")