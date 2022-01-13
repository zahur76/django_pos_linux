from django.shortcuts import get_object_or_404

from products.models import Product


def bag_contents(request):

    bag = request.session.get("bag", [])

    bag_items = []

    net_total = 0
    vat_total = 0
    vat = 0
    for item in bag:
        product = get_object_or_404(Product, id=item["id"])
        item["product"] = product
        item["sub_total"] = product.price * item["quantity"]
        bag_items.append(item)
        net_total += item["quantity"] * product.price
        if product.has_vat:
            vat_total += item["quantity"] * product.price

        vat = vat_total * 0.15

    context = {
        "bag_content": bag_items,
        "net_total": net_total,
        "vat": round(vat, 3),
        "grand_total": net_total + vat,
    }
    return context
