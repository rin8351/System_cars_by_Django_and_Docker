from django.contrib import admin
from django.urls import path
from django.urls import include
from carsdb.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('carsdb.urls')),
]
