from asyncio.windows_events import NULL
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from datetime import datetime
from django.utils.timezone import now
from django.db.models import Sum

from carmechanic.forms import AppRatingForm, MechanicRatingForm

from django.db.models import Avg
from .models import AppRating, BookedMechanic, Booking, Cart, ForgotPassword, Mechanic, Notification, UserPassword, User, CarPart, Wishlist, Transaction, Checkout, MechanicRating

# Create your views here.
def index(request):
    return render(request, "carmechanic/index.html")

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "carmechanic/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "carmechanic/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        forgotpassword = UserPassword(usernames=username)

        forgotpassword.usernames = request.POST["username"]
        forgotpassword.firstname = request.POST["first_name"]
        forgotpassword.lastname = request.POST["last_name"]
        forgotpassword.password1 = request.POST["password"]
        forgotpassword.security1 = request.POST["security1"]
        forgotpassword.security2 = request.POST["security2"]
        forgotpassword.security3 = request.POST["security3"]
        forgotpassword.save() 

        if password != confirmation:
            return render(request, "carmechanic/signup.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "carmechanic/signup.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "carmechanic/signup.html")

def forgotpassword(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        userpassword = UserPassword.objects.get(usernames=username)
        forgotpassword = ForgotPassword(usernames=username)

        forgotpassword.security1 = request.POST["security1"]
        forgotpassword.security2 = request.POST["security2"]
        forgotpassword.security3 = request.POST["security3"]
        forgotpassword.newpassword = request.POST["password"]
        forgotpassword.save()

        
        if ((userpassword.security1 != forgotpassword.security1) | (userpassword.security2 != forgotpassword.security2) | (userpassword.security3 != forgotpassword.security3)): 
            return render(request, "carmechanic/forgotpassword.html", {
                "message": "Security question is incorrect."
            })
        else:
            user = User.objects.get(username__exact=username)
            user.set_password(password)
            user.save()
            return render(request, "carmechanic/login.html", {
                "message": "Password changed successfully"
            })

    else:
        return render(request, "carmechanic/forgotpassword.html")

def carparts(request):
    carpart = CarPart.objects.all()
    try:
        addtocart = Cart.objects.filter(buyer=request.user.username)
        addtocartcount=len(addtocart)
    except:
        addtocartcount=None
    return render(request, "carmechanic/carparts.html", {
        'object': carpart,
        'addtocartcount': addtocartcount
    })

def mechanics(request):
    mechanic = Mechanic.objects.all()
    try:
        addtocart = Cart.objects.filter(buyer=request.user.username)
        addtocartcount=len(addtocart)
    except:
        addtocartcount=None
    return render(request, "carmechanic/mechanics.html", {
        'object': mechanic,
        'addtocartcount': addtocartcount
    })

def userinfo(request):
    userinfo = UserPassword.objects.filter(usernames=request.user.username)
    return render(request, "carmechanic/userInfo.html", {
        'userinfo': userinfo
    })

def carpartpage(request,id):
    carpart = CarPart.objects.get(id=id)
    if request.user.username:
        try:
            if Cart.objects.get(buyer=request.user.username, listingid=id):
                addedtocart=True
        except:
            addedtocart = False
        try:
            cart = Cart.objects.filter(buyer=request.user.username)
            cartcount = len(cart)
        except:
            cartcount=None
        try:
            if Wishlist.objects.get(buyer=request.user.username, listingid=id):
                addedtowishlist=True
        except:
            addedtowishlist = False
        try:
            cart = Wishlist.objects.filter(buyer=request.user.username)
            wishlistcount = len(cart)
        except:
            wishlistcount=None
    else:
        addedtocart = False
        addedtowishlist = False
        cartcount = None
        wishlistcount= None
    return render(request, "carmechanic/carpartlisting.html", {
        'object': carpart,
        'addedtocart': addedtocart,
        "cartcount": cartcount,
        'addedtowishlist': addedtowishlist,
        "wishlistcount": wishlistcount,
        "error":request.COOKIES.get('error'),
        "success":request.COOKIES.get('success'),
    })

def mechanicpage(request,id):
    mechanic = Mechanic.objects.get(id=id)
    rating = MechanicRating.objects.filter(listingid=id)
    try:
        ratingform = MechanicRatingForm(request.POST or None)
    except:
        return redirect('index')
    if request.user.username:
        try:
            if Mechanic.objects.get(buyer=request.user.username, listingid=id):
                added=True
        except:
            added = False
        try:
            ratingcount = MechanicRating.objects.filter(listingid=id)
            ratingcount = len(ratingcount)
        except:
            ratingcount = len(ratingcount)
        try:
            if mechanic.lister == request.user.username :
                lister = True
            else:
                lister = False
        except:
            return redirect('index')
    else:
        ratingcount = MechanicRating.objects.filter(listingid=id)
        ratingcount = len(ratingcount)
        added = False
        lister = False
    return render(request, "carmechanic/mechaniclisting.html", {
        'object': mechanic,
        'added': added,
        'lister': lister,
        'rating': rating,
        'ratingcount': ratingcount,
        'ratingform': ratingform,
        "error":request.COOKIES.get('error'),
        "success":request.COOKIES.get('success'),
    })

@login_required
def addtocart(request, id):
    if request.user.username:
        carpart = CarPart.objects.get(id=id)
        buyers = Cart(buyer = request.user.username, listingid = id)
        buyers.prices = carpart.prices
        buyers.productnames = carpart.productnames
        buyers.images = carpart.images
        buyers.save()
        return redirect('carpartpage', id=id)
    else:
        return redirect('index')

@login_required
def removetocart(request,id):
    if request.user.username:
        try:
            Cart.objects.filter(listingid=id).delete()
            return redirect('carpartpage', id=id)
        except:
            return redirect('carpartpage', id=id)
    else:
        return redirect('index')

@login_required
def cart(request):
    try:
        cart = Cart.objects.filter(buyer=request.user.username)
        cartcount = len(cart)                #count how many rows in table Cart using len()
        total = sum(cart.values_list('prices', flat=True))
    except:
        cartcount = None
        total = None
    return render(request, "carmechanic/cart.html", {
        'object': cart,
        "cartcount": cartcount,
        "total": total
    })

@login_required
def bookmechanic(request, listingid):
    if request.user.username:
        try:
            mechanic = Mechanic.objects.get(id=listingid)
        except:
            return redirect('index')

        bookmechanic = BookedMechanic(listingid=listingid)
        name = mechanic.mechanics
        bookmechanic.listingid = listingid
        bookmechanic.buyer = request.user.username
        bookmechanic.mechanics = mechanic.mechanics
        bookmechanic.locations = mechanic.locations
        bookmechanic.rates = mechanic.rates
        bookmechanic.images = mechanic.images
        bookmechanic.save()

        transactionhistory = Transaction(listingid=listingid)
        transactionhistory.mechanics = mechanic.mechanics
        transactionhistory.rates = mechanic.rates
        transactionhistory.listingid = listingid
        transactionhistory.buyer = request.user.username
        transactionhistory.created = datetime.now()
        transactionhistory.save()


        return render(request,"carmechanic/booking.html",{
            'bookmechanic': bookmechanic,
            "name": name
        })
    else:
        return redirect('index')

@login_required
def addtowishlist(request, id):
    if request.user.username:
        wishlist = CarPart.objects.get(id=id)
        buyers = Wishlist(buyer = request.user.username, listingid = id)
        buyers.prices = wishlist.prices
        buyers.productnames = wishlist.productnames
        buyers.images = wishlist.images
        buyers.save()
        return redirect('carpartpage', id=id)
    else:
        return redirect('index')

@login_required
def removetowishlist(request,id):
    if request.user.username:
        try:
            Wishlist.objects.filter(listingid=id).delete()
            return redirect('carpartpage', id=id)
        except:
            return redirect('carpartpage', id=id)
    else:
        return redirect('index')

@login_required
def wishlist(request):
    try:
        wishlist = Wishlist.objects.filter(buyer=request.user.username)
        wishcount = len(wishlist)                                                 #count how many rows in table Watchlist using len()
    except:
        wishcount = None
    return render(request, "carmechanic/wishlist.html", {
        'object': wishlist,
        "watchcount": wishcount,
    })

@login_required
def bookmechanic(request, listingid):
    if request.user.username:
        try:
            mechanic = Mechanic.objects.get(id=listingid)
        except:
            return redirect('index')

        bookmechanic = BookedMechanic(listingid=listingid)
        name = mechanic.mechanics
        bookmechanic.listingid = listingid
        bookmechanic.buyer = request.user.username
        bookmechanic.mechanics = mechanic.mechanics
        bookmechanic.locations = mechanic.locations
        bookmechanic.rates = mechanic.rates
        bookmechanic.images = mechanic.images
        bookmechanic.save()

        transactionhistory = Transaction(listingid=listingid)
        transactionhistory.mechanics = mechanic.mechanics
        transactionhistory.prices = mechanic.rates
        transactionhistory.listingid = listingid
        transactionhistory.buyer = request.user.username
        transactionhistory.created = datetime.now()
        transactionhistory.save()


        return render(request,"carmechanic/booking.html",{
            'bookmechanic': bookmechanic,
            "name": name
        })
    else:
        return redirect('index')

@login_required
def checkout(request):
    if request.user.username:
        try:
            cart = Cart.objects.filter(buyer=request.user.username)
            totalCart = sum(cart.values_list('prices', flat=True))
        except:
            return redirect('index')

        checkout = Checkout(buyer=request.user.username)
        checkout.buyer = request.user.username
        checkout.price = totalCart + 50
        total = checkout.price
        checkout.save()

        transactionhistory = Transaction(buyer=request.user.username)
        transactionhistory.prices = totalCart + 50
        transactionhistory.buyer = request.user.username
        transactionhistory.created = datetime.now()
        transactionhistory.save()

        return render(request,"carmechanic/checkout.html",{
            'object': cart,
            'checkout': checkout,
            "total": total,
            "totalCart": totalCart
        })
    else:
        return redirect('index')

def backtohome(request):
    if request.user.username:
        try:
            cart = Cart.objects.filter(buyer=request.user.username)
        except:
            return redirect('index')

        cart.delete()
        return render(request,"carmechanic/cart.html",{
            'object': cart
        })
    else:
        return redirect('index')

def deletetransactions(request):
    if request.user.username:
        try:
            cart = Transaction.objects.filter(buyer=request.user.username)
        except:
            return redirect('index')

        cart.delete()
        return render(request,"carmechanic/transactionhistory.html",{
            'object': cart
        })
    else:
        return redirect('index')

@login_required
def transactionhistory(request):
    try:
        transactionhistory = Transaction.objects.filter(buyer=request.user.username)
        transactioncount = len(transactionhistory)                                                 #count how many rows in table Watchlist using len()
    except:
        transactioncount = None
    return render(request, "carmechanic/transactionhistory.html", {
        'object': transactionhistory,
        "transactioncount": transactioncount,
    })

@login_required
def notification(request):
    try:
        notification = Notification.objects.all()
        notificationcount=len(addtocart)
    except:
        notificationcount=None
    return render(request, "carmechanic/notification.html", {
        'object': notification,
        'addtocartcount': notificationcount
    })

@login_required
def createapprating(request):
    creator = AppRating.objects.all()
    form = AppRatingForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            now = datetime.now()                                                #save date created with current timezone
            fs = form.save(commit=False)
            fs.lister = request.user                                            #save info not listed at forms.py
            fs.created = now
            fs.save()
        return HttpResponseRedirect(reverse('viewapprating'))
    else:
        return render(request, "carmechanic/createapprating.html", {
            'form': form,
            'creator': creator
        })

def viewapprating(request):
    try:
        apprating = AppRating.objects.all()
        appratingcount=len(apprating)

        averageapprating = (sum(apprating.values_list('ratings', flat=True)) / appratingcount)
    except:
        appratingcount=None
        averageapprating=None
    return render(request, "carmechanic/viewapprating.html", {
        'object': apprating,
        'addtocartcount': appratingcount,
        'averageapprating': averageapprating
    })

def viewmechanicrating(request):
    try:
        ratingjose = MechanicRating.objects.filter(mechanics='Jose Rizal')
        ratingjosecount=len(ratingjose)
        averagejose= (sum(ratingjose.values_list('ratings', flat=True)) / ratingjosecount)
    except:
        ratingjosecount=None
        averagejose=None
    try:
        ratingjohn = MechanicRating.objects.filter(mechanics='John Doe')
        ratingjohncount=len(ratingjohn)
        averagejohn= (sum(ratingjohn.values_list('ratings', flat=True)) / ratingjohncount)
    except:
        ratingjohncount=None
        averagejohn=None
        ratingjohn=None
    try:
        ratingpedro = MechanicRating.objects.filter(mechanics='San Pedro')
        ratingpedrocount=len(ratingpedro)
        averagepedro= (sum(ratingpedro.values_list('ratings', flat=True)) / ratingpedrocount)
    except:
        ratingpedro = None
        ratingpedrocount=None
        averagepedro=None
    try:
        ratingryan = MechanicRating.objects.filter(mechanics='Ryan Soliguen')
        ratingryancount=len(ratingryan)
        averageryan= (sum(ratingryan.values_list('ratings', flat=True)) / ratingryancount)
    except:
        ratingryan = None
        ratingryancount=None
        averageryan= None
    return render(request, "carmechanic/viewmechanicrating.html", {
        'ratingjohn': ratingjohn,
        'averagejohn': averagejohn,
        'ratingjose': ratingjose,
        'averagejose': averagejose,
        'ratingpedro': ratingpedro,
        'averagepedro': averagepedro,
        'ratingryan': ratingryan,
        'ratingryancount': ratingryancount,
        'averageryan': averageryan
    })
    

# @login_required
# def createmechanicrating(request, listingid):
#     if request.method == "POST":
#         mechanicratings = MechanicRating.objects.all()
#         ratingform = MechanicRatingForm(request.POST or None)

#         try:
#             mechanic = Mechanic.objects.get(id=id)
#             rating = MechanicRating.objects.filter(listingid=id)
#             appratingcount=len(rating)

#             averageapprating = (sum(rating.values_list('ratings', flat=True)) / appratingcount)

#             mechanic.ratings = averageapprating
#             mechanic.save()
#         except:
#             appratingcount=None
#             averageapprating=None
#         if ratingform.is_valid():
#             now = datetime.now()
#             fs = ratingform.save(commit=False)
#             fs.listingid = listingid
#             fs.lister = request.user.username
#             fs.created = now
#             fs.save()
#         return redirect('mechanicpage', id=listingid)
#     else:
#         return redirect('index')

@login_required
def createmechanicrating(request):
    mechanicratings = MechanicRating.objects.all()
    ratingform = MechanicRatingForm(request.POST or None)
    if request.method == "POST":
        if ratingform.is_valid():
            now = datetime.now()                                                #save date created with current timezone
            fs = ratingform.save(commit=False)
            fs.lister = request.user                                            #save info not listed at forms.py
            fs.created = now
            fs.save()
        return HttpResponseRedirect(reverse('viewmechanicrating'))
    else:
        return render(request, "carmechanic/createmechanicrating.html", {
            'form': ratingform,
            'mechanicratings': mechanicratings
        })