from.import views
from django.urls import path



urlpatterns = [
    path('marketplace', views.marketplace, name='marketplace'),
    path('<slug:vendor_slug>/',views.vendor_details,name='vendor_details'),
    path('add_to_cart/<int:food_id>/',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:food_id>/',views.remove_from_cart,name='remove_from_cart'),
]
