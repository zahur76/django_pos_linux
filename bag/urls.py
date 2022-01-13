from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("add_to_bag/<int:product_id>", views.add_to_bag, name="add_to_bag"),
    path(
        "delete_from_bag/<int:product_id>",
        views.delete_from_bag,
        name="delete_from_bag",
    ),
]
