from django.urls import path
from .views import *

app_name = 'ysapp'
urlpatterns = [
    path('', anasayfa, name="anasayfa"),
] 