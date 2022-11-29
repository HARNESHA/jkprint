from django.contrib import admin
from django.urls import path,include
from JKPrintapp import views

urlpatterns = [
   path('',views.index),
   path('usersignup/',views.usersignup),
   path('home/',views.home,name='home'),
   path('papercost/',views.papercost,name='papercost'),
   path('final/',views.final,name='final'),
]
