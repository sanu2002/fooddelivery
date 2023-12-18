from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.myaccount, name='myaccount'),
    path('registerUser/', views.registerUser, name='registerUser'),
    path('registerVendor/', views.registerVendor, name='registerVendor'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('vendashboard/', views.vendashboard, name='vendashboard'),
    path('customerdashboard/', views.customerdashboard, name='customerdashboard'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),  # added '/' at the end
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetpassword/', views.resetpassword, name='resetpassword'),
    path('accounts/', include('vendor.urls')),  # corrected the include statement
]