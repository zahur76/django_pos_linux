from django.urls import path

from . import views

urlpatterns = [
    path("category", views.category, name="category"),
    path("category_delete/<int:category_id>", views.category_delete, name="category_delete"),
]