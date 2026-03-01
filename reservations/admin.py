from django.contrib import admin
from .models import Reservation, Reservation_date, Reservation_request

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'cabin', 'dishes_order1', 'dishes_order2')
    search_fields = ('user__email', 'date', 'cabin__name')
    list_filter = ('date', 'cabin')
    ordering = ('-date',)
    list_per_page = 10

@admin.register(Reservation_date)
class Reservation_dateAdmin(admin.ModelAdmin):
    list_display = ('date', 'available')
    list_editable = ('available',)
    search_fields = ('date',)
    list_filter = ('available',)
    ordering = ('-date',)
    list_per_page = 10

@admin.register(Reservation_request)
class Reservation_requestAdmin(admin.ModelAdmin):
    list_display = ('user', 'checkin', 'checkout', 'date')
    search_fields = ('user__email', 'cabin__name')
    ordering = ('-date',)
    list_per_page = 10