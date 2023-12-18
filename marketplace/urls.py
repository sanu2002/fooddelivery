from.import views
from django.urls import path



urlpatterns = [
    path('marketplace', views.marketplace, name='marketplace'),
]
