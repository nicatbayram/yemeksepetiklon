from django.urls import path
from .views import *

app_name = 'ysapp'
urlpatterns = [
    path('', anasayfa, name="anasayfa"),
    path('restoranlar/', RestoranListView.as_view(), name='restoranlar'),
    path('restoranlar/<int:pk>/', RestoranDetailView.as_view(), name="restorandetay"),
    path('restoranlar/olustur/', RestoranCreateView.as_view(), name="restoranolustur"),
    path('restoranlar/<int:pk>/yemek/', YemekAddView.as_view(), name= 'yemekadd')



] 