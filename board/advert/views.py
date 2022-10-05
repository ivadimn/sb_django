from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def advert_list(request, *args, **kwargs):
    return render(request, "advert/advert_list.html", {})


def advert1_list(request, *args, **kwargs):
    return render(request, "advert/advert1_list.html", {})

