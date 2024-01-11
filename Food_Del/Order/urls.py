from django.urls import path
from . import views
urlpatterns=[
	path('Orders/',views.Orders,name="Orders"),
	path('Orders/PlaceOrd/',views.PlaceOrd,name="PlaceOrd/"),
	path('cart',views.cart,name="cart")	
]