from django.contrib import admin
from .models import CarPart, Cart, Checkout, Mechanic, Wishlist, BookedMechanic, Booking, Transaction, Notification, AppRating, MechanicRating, UserPassword, ForgotPassword

# Register your models here.

class CarPartAdmin(admin.ModelAdmin):
    list_display = ("__str__", "productnames")

class MechanicAdmin(admin.ModelAdmin):
    list_display = ("__str__", "buyer")

class CheckoutAdmin(admin.ModelAdmin):
    list_display = ("__str__", "price")

class CartAdmin(admin.ModelAdmin):
    list_display = ("__str__", "buyer")

class WishlistAdmin(admin.ModelAdmin):
    list_display = ("__str__", "buyer")

class BookedMechanicAdmin(admin.ModelAdmin):
    list_display = ("__str__", "buyer")

class BookingAdmin(admin.ModelAdmin):
    list_display = ("__str__", "buyer")

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "buyer")

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title")

class AppRatingAdmin(admin.ModelAdmin):
    list_display = ("__str__", "lister")

class MechanicRatingAdmin(admin.ModelAdmin):
    list_display = ("__str__", "lister")

class PasswordAdmin(admin.ModelAdmin):
    list_display = ("__str__", "usernames")

class ForgotPasswordAdmin(admin.ModelAdmin):
    list_display = ("__str__", "usernames")

admin.site.register(CarPart, CarPartAdmin)
admin.site.register(Mechanic, MechanicAdmin)
admin.site.register(Checkout, CheckoutAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(BookedMechanic, BookedMechanicAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Notification, NotificationsAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(AppRating, AppRatingAdmin)
admin.site.register(MechanicRating, MechanicRatingAdmin)
admin.site.register(UserPassword, PasswordAdmin)
admin.site.register(ForgotPassword, ForgotPasswordAdmin)
