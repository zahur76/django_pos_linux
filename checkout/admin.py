from django.contrib import admin

from .models import Order, OrderLineItem

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    # what to be displayed in admin
    list_display = (
        "id",
        "order_number",
        "created_at",
    )


class OrderLineItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
    )


# The model followed by class name (model, class name)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem, OrderLineItemAdmin)
