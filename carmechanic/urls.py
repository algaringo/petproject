from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup, name="signup"),
    path("carparts", views.carparts, name="carparts"),
    path("mechanics", views.mechanics, name="mechanics"),
    path("userinfo", views.userinfo, name="userinfo"),
    path("cart", views.cart, name="cart"),

    path("checkout", views.checkout, name="checkout"),
    path("backtohome", views.backtohome, name="backtohome"),
    path("transactionhistory", views.transactionhistory, name="transactionhistory"),
    path("notification", views.notification, name="notification"),
    path("deletetransactions", views.deletetransactions, name="deletetransactions"),


    path("carparts/<int:id>", views.carpartpage, name="carpartpage"),
    path("carparts/<int:id>/addtocart", views.addtocart, name="addtocart"),
    path("carparts/<int:id>/removetocart",views.removetocart,name="removetocart"),
    # path("listing/<int:listingid>/bid",views.bid,name="bid"),

    path("wishlist", views.wishlist, name="wishlist"),
    path("carparts/<int:id>/addtowishlist", views.addtowishlist, name="addtowishlist"),
    path("carparts/<int:id>/removetowishlist",views.removetowishlist,name="removetowishlist"),


    path("mechanic/<int:id>", views.mechanicpage, name="mechanicpage"),
    path("mechanic/<int:listingid>/bookmechanic", views.bookmechanic, name="bookmechanic"),
]