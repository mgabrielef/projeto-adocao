from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', viewHome, name='home'),
    path('addAbrigo', viewAddAbrigo, name='addAbrigo'),
    path('detailsAbrigo/<int:id>', viewAbrigoDetails, name='detailsAbrigo'),
    path('deleteAbrigo/<int:id>', viewDeleteAbrigo, name='deleteAbrigo'),
    path('updateAbrigo/<int:id>', viewUpdateAbrigo, name='updateAbrigo'),
    path('listPets', viewListPets, name='listPets'),
    path('addPet', viewAddPet, name='addPet'),
    path('detailsPet/<int:id>', viewPetDetails, name='detailsPet'),
    path('deletePet/<int:id>', viewDeletePet, name='deletePet'),
    path('updatePet/<int:id>', viewUpdatePet, name='updatePet'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)