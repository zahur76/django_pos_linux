from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.translate, name="translate"),
    path("/menu_language", views.menu_language, name="menu_language"),
]
