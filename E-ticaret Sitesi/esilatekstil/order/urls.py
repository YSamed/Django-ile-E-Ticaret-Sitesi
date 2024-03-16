from django.urls import path
from . import views


app_name = 'order'
urlpatterns = [
    path('', views.index, name='index'),
    path('addtocart/<int:id>', views.addtocart, name='addtocart'),
    path('addtocart/<int:id>/', views.addtocart, name='addtocart'),
    path('order/addtocart/<int:id>/', views.addtocart, name='add_to_cart'),
]