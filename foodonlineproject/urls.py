"""
URL configuration for foodonlineproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


from marketplace import views as Maeketviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('accounts/',include('accounts.urls')),
    path('vendor/',include('vendor.urls')),
    path('menuapp/',include('menuapp.urls')),
    path('marketplace/',include('marketplace.urls')),
    path('customer/',include('customer.urls')),
    
    path('cart/',Maeketviews.cart,name='cart'),
    path('search/',Maeketviews.search,name='search')
    # path("__debug__/", include("debug_toolbar.urls")),
    # path('geoocode/',views.geoocode)
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


