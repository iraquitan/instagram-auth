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
        "client_id": (None, settings.CLIENT_ID),
        "client_secret": (None, settings.CLIENT_SECRET),
        "grant_type": (None, "authorization_code"),
        "redirect_uri": (None, settings.AUTHORIZATION_REDIRECT_URI),
        "code": (None, code),
    }
    response = requests.post(
        "https://api.instagram.com/oauth/access_token", files=files
    )

    if response.status_code == 200:
        # Add user access token to database
        context = response.json()
        user = InstagramUser(
            access_token=context["access_token"],
            username=context["user"]["username"],
            full_name=context["user"]["full_name"],
            profile_picture=context["user"]["profile picture"],
            social_id=context["user"]["id"],
        )
        user.save()
        return render(request, "getauth/callback.html", context=context)
    else:
        return render(request, "getauth/callback.html")
