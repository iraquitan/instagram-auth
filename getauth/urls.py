from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("callback/", views.callback, name="callback"),
    path("instafeed/<str:username>", views.instafeed, name="instafeed"),
]
