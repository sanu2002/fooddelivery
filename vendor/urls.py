from django.urls import path 
from.import views

from  accounts import  views as accountview




urlpatterns = [
    path('',accountview.vendashboard,name='vendor'),
    path('profile/',views.vprofile,name='vprofile'),
    path('menu_builder/',views.menu_builder,name='menu_builder'),
    path('add_category/',views.add_category,name='add_category'),
    path('addfood_bycat/<int:pk>/',views.addfood_bycat,name='addfood_bycat'),
    path('update/<int:pk>/', views.cat_update, name='update'),
    path('delete/<int:pk>/', views.cat_delete, name='delete'),
    path('food_delete/<int:id>/', views.food_delete, name='food_delete'),
    path('add_food',views.add_food,name='add_food'),
    path('food_update/<int:pk>/',views.food_update,name='food_update'),
    path('opening_hour/',views.opening_hour,name='opening_hour'),
    path('opening_hour/add',views.add_opening_hour,name='add_opening_hour'),
    path('openinghour_delete/<int:pk>/',views.openinghour_delete,name='openinghour_delete'),
    

    # path('vendor_update/',views.vendor_update,name='vendor_update'),
    
]


# '''OR ELSE YOU CAN HANDLE THE UPDATE HERE'''