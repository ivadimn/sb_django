from django.urls import path
from . import views

urlpatterns = [
    path("", views.advert_list, name="advert_list"),
    path("advert1", views.advert1, name="advert1"),

]