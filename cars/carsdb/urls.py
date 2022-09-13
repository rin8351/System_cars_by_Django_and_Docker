from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('parts/', views.parts_f, name='parts'),
    path('cars/', views.cars_f, name='cars'),
    path('addcars/', views.addcars_f.as_view(), name='add_cars'),
    path('addparts/', views.addparts_f.as_view(), name='add_parts'),
    path('acessor/', views.acces_f, name='acessor'),
    path('register/', views.register.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    ]
