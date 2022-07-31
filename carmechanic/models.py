from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from django.utils.timezone import now

# Create your models here.
class User(AbstractUser):
    pass

class CarPart(models.Model): 
    productnames = models.CharField(max_length=20)
    descriptions = models.TextField(max_length=500, blank=True, null=True)
    prices = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    images = models.URLField(blank=True, null=True)
    lister = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.productnames

class Mechanic(models.Model): 
    mechanics = models.CharField(max_length=20)
    locations = models.CharField(max_length=20, blank=True, null=True)
    introductions = models.TextField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    rates = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ratings = models.IntegerField(blank=True, null=True)
    images = models.URLField(blank=True, null=True)
    lister = models.CharField(max_length=50, blank=True, null=True)
    buyer = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(default=now, editable=False)
    listingid = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.listingid}"

class Cart(models.Model):
    productnames = models.CharField(max_length=20)
    mechanics = models.CharField(max_length=20, blank=True, null=True)
    images = models.URLField(blank=True, null=True)
    prices = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    lister = models.CharField(max_length=50, blank=True, null=True)
    buyer = models.CharField(max_length=50, blank=True, null=True)
    listingid = models.IntegerField()

    def __str__(self):
        return f"{self.listingid}"

class Wishlist(models.Model):
    productnames = models.CharField(max_length=20)
    mechanics = models.CharField(max_length=20, blank=True, null=True)
    images = models.URLField(blank=True, null=True)
    prices = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    lister = models.CharField(max_length=50, blank=True, null=True)
    buyer = models.CharField(max_length=50, blank=True, null=True)
    listingid = models.IntegerField()

    def __str__(self):
        return f"{self.listingid}"

class Checkout(models.Model):
    productnames = models.CharField(max_length=20, blank=True, null=True)
    images = models.URLField(blank=True, null=True)
    buyer = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    listingid = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.listingid}"

class Booking(models.Model):
    mechanics = models.CharField(max_length=20)
    buyer = models.CharField(max_length=50, blank=True, null=True)
    rates = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    listingid = models.IntegerField()

    def __str__(self):
        return f"{self.listingid}"

class BookedMechanic(models.Model):
    mechanics = models.CharField(max_length=20)
    locations = models.CharField(max_length=20, blank=True, null=True)
    images = models.URLField(blank=True, null=True)
    lister = models.CharField(max_length=64, blank=True, null=True)
    buyer = models.CharField(max_length=64, blank=True, null=True)
    rates = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    listingid = models.IntegerField()

    def __str__(self):
        return f"{self.listingid}"

class Transaction(models.Model):
    mechanics = models.CharField(max_length=20)
    productnames = models.CharField(max_length=20, blank=True, null=True)
    buyer = models.CharField(max_length=50, blank=True, null=True)
    rates = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    prices = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    created = models.DateTimeField(default=now, editable=False)
    listingid = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.listingid}"

class AppRating(models.Model): 
    ratings = models.IntegerField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(max_length=500, blank=True, null=True)
    lister = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.productnames

class Notification(models.Model):
    title= models.CharField(max_length=30)
    images = models.URLField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.title