from django.contrib import admin
from . import models


class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "no_of_guests", "booking_date")


class MenuAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "inventory")


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "inventory")


# Register your models here.
admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.Booking, BookingAdmin)
admin.site.register(models.MenuItem, MenuItemAdmin)
