from django.urls import path
from .views import *

app_name = 'ysapp'
urlpatterns = [
    path('', anasayfa, name="anasayfa"),
    # path('', restoran, name='restoranlar'),
    # path('restoranlar/<int:pk>/', restoranlar.as_view(), name="restorandetay"),
] 