from django.urls import path , include
from . import views 



app_name = 'homeapp'

urlpatterns = [
    path('', views.index, name='index'),
] 



