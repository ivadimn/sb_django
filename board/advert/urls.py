from django.urls import path
from . import views

urlpatterns = [
    path("advert", views.advert_list, name="advert_list"),
    path("advert1", views.advert1, name="advert1"),
    path("advert2", views.advert2, name="advert2"),
    path("advert3", views.advert3, name="advert3"),
    path("advert4", views.advert4, name="advert4"),
    path("advert5", views.advert5, name="advert6"),

]