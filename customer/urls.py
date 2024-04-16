from django.urls import path
from .import views


urlpatterns = [
    path('customerprofile/',views.customerprofile,name='customerprofile')
]
