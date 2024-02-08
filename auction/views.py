from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from auction.models import Auction


def render_range():
    return range(10)


def index(request: HttpRequest):
    return render(request, "index.html")


def auction_list(request: HttpRequest):
    auction_list = Auction.objects.all()
    context = {
        "auction_list": auction_list
    }
    return render(request, "auction-list.html", context=context)

def profile(request: HttpRequest):
    return render(request, "profile.html")

def sign_up(request: HttpRequest):
    return render(request, "sign-up.html")

def sign_in(request: HttpRequest):
    return render(request, "sign-in.html")
