from django.shortcuts import render
import json
import requests

# Create your views here.
def index(request):
    return render(request, "getauth/index.html")


def callback(request):
    code = request.GET.get("code", None)
    # context = {"code": code}

    files = {
        "client_id": (None, "CLIENT_ID"),
        "client_secret": (None, "CLIENT_SECRET"),
        "grant_type": (None, "authorization_code"),
        "redirect_uri": (None, "AUTHORIZATION_REDIRECT_URI"),
        "code": (None, "CODE"),
    }
    response = requests.post(
        "https://api.instagram.com/oauth/access_token", files=files
    )
    # context = json.loads(response.json())
    context = response.json()
    print(context)

    return render(request, "getauth/callback.html", context=context)
