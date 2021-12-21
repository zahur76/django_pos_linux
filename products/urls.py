from django.urls import path

from . import views

urlpatterns = [
    path("category", views.category, name="category"),
    path("subcategory", views.subcategory, name="subcategory"),
    path(
        "category_delete/<int:category_id>",
        views.category_delete,
        name="category_delete",
    ),
    path("category_edit/<int:category_id>", views.category_edit, name="category_edit"),
    path(
        "add_subcategory/<str:category_name>",
        views.add_subcategory,
        name="add_subcategory",
    ),
    path(
        "delete_subcategory/<int:subcategory_id>",
        views.delete_subcategory,
        name="delete_subcategory",
    ),
    path(
        "edit_subcategory/<int:subcategory_id>",
        views.edit_subcategory,
        name="edit_subcategory",
    ),
    path("products", views.products, name="products"),
    path("add_product/<int:category_id>", views.add_product, name="add_product"),
    path(
        "delete_product/<int:product_id>", views.delete_product, name="delete_product"
    ),
    path(
        "update_product/<int:product_id>", views.update_product, name="update_product"
    ),
]
