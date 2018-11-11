import json

import requests
from django.shortcuts import render
from django.conf import settings

from .models import InstagramUser


# Create your views here.
def index(request):
    context = {
        "button_href": f"https://api.instagram.com/oauth/authorize/?client_id={ settings.CLIENT_ID }&redirect_uri={settings.AUTHORIZATION_REDIRECT_URI}&response_type=code"
    }
    return render(request, "getauth/index.html", context=context)


def callback(request):
    code = request.GET.get("code", None)

    files = {
        "client_id": settings.CLIENT_ID,
        "client_secret": settings.CLIENT_SECRET,
        "grant_type": "authorization_code",
        "redirect_uri": settings.AUTHORIZATION_REDIRECT_URI,
        "code": code,
    }
    response = requests.post("https://api.instagram.com/oauth/access_token", data=files)

    if response.status_code == 200:
        # Add user access token to database
        context = response.json()
        user = InstagramUser(
            access_token=context["access_token"],
            username=context["user"]["username"],
            full_name=context["user"]["full_name"],
            profile_picture=context["user"]["profile_picture"],
            social_id=context["user"]["id"],
        )
        user.save()
        return render(request, "getauth/callback.html", context=context)
    else:
        context = {"error_content": response.text}
        return render(request, "getauth/error.html", context=context)


def instafeed(request, username):
    user = InstagramUser.objects.filter(username=username).first()
    context = {"user": user}
    return render(request, "getauth/instafeed.html", context=context)
