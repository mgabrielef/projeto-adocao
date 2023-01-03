from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', viewHome, name='home'),
    path('addAbrigo', viewAddAbrigo, name='addAbrigo'),
    path('detailsAbrigo', viewAbrigoDetails, name='detailsAbrigo'),
    path('listarAbrigos', viewGetAbrigo, name='listarAbrigos')
] 