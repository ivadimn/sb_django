from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def advert_list(request, *args, **kwargs):
    return render(request, "advert/advert_list.html", {})


def advert1(request, *args, **kwargs):
    return render(request, "advert/advert1.html", {})


def advert2(request, *args, **kwargs):
    return render(request, "advert/advert2.html", {})


def advert3(request, *args, **kwargs):
    return render(request, "advert/advert3.html", {})


def advert4(request, *args, **kwargs):
    return render(request, "advert/advert4.html", {})


def advert5(request, *args, **kwargs):
    return render(request, "advert/advert5.html", {})
