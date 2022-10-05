from django.urls import path
from . import views

urlpatterns = [
    path("advert", views.advert_list, name="advert_list"),
    path("advert1", views.advert1_list, name="advert1_list")
]