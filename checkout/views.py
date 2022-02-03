from django.shortcuts import get_object_or_404, render, redirect, reverse

from bag.contexts import bag_contents
from checkout.models import Order, OrderLineItem
from products.models import Product


# Create your views here.
def checkout(request):
    if request.POST:
    
        basket = request.session.get("bag", {})

        if basket == {}:
            return redirect(reverse("home"))

        bag_items = []

        net_total = 0
        vat_total = 0
        vat = 0
        for item in basket:
            product = get_object_or_404(Product, id=item["id"])
            item["product"] = product
            item["sub_total"] = product.price * item["quantity"]
            bag_items.append(item)
            net_total += item["quantity"] * product.price
            if product.has_vat:
                vat_total += item["quantity"] * product.price

            vat = vat_total * 0.15
        order = Order(net_total=net_total, vat=vat, gross_total=net_total + vat)
        order.save()
        for item in bag_items:
            if item["product"].has_vat:
                vat = item["quantity"] * item["product"].price * 0.15
            else:
                vat = 0
            if item["product"].colour_available:
                colour = item["colour"]
            else:
                colour = "none"
            if item["product"].sizes_available:
                size = item["size"]
            else:
                size = "none"
            line_item = OrderLineItem(
                order=order,
                product=get_object_or_404(Product, id=item["id"]),
                size=size,
                colour=colour,
                quantity=item["quantity"],
                lineitem_total=item["quantity"] * item["product"].price,
                lineItem_vat=vat,
            )
            line_item.save()

            if 'bag' in request.session:
                del request.session['bag']
        
        line_items = OrderLineItem.objects.filter(order=order.id)
        context = {'order': order,
                    'items': line_items,
                }

        return render(request, "checkout/checkout.html", context)


def order(request):

    orders = Order.objects.all()

    context = {'orders': orders}

    return render(request, "checkout/order.html", context)