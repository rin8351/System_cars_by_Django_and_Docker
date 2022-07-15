from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('parts/', views.parts_f, name='parts'),
    path('cars/', views.cars_f, name='cars'),
    path('addcars/', views.addcars_f.as_view(), name='add_cars'),
    path('addparts/', views.addparts_f.as_view(), name='add_parts'),
    path('acessor/', views.acces_f, name='acessor'),
    ]