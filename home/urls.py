from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('home/', views.home, name="home"),
	path('Restaurants/', views.Restaurants, name="Restaurants"),
	path('about/', views.about, name="about"),
    path('Contact/', views.Contact, name="Contact"),
	path('loginn/', views.user_Login, name="loginn"),
	path('Signup/', views.Signup, name="Signup"),
    path('cart/', views.cart, name="cart"),
	path('checkout/', views.Checkout, name="checkout"),
	path('update_item/', views.updateItem, name="updateitem"),
	path('singleitem/', views.Singleitem, name="singleitem"),
]