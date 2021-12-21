from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.translate, name="translate"),
    path("change_language", views.change_language, name="change_language"),
]