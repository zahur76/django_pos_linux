from django.shortcuts import get_list_or_404, redirect, render, reverse

from products.models import Product


# Create your views here
def add_to_bag(request, product_id):
    """A view to add products to bag"""

    bag = request.session.get("bag", [])

    product = get_list_or_404(Product, id=product_id)

    if request.POST:
        try:
            request.POST["colour"]
            colour = request.POST["colour"]
        except:
            colour = False
        try:
            request.POST["size"]
            size = request.POST["size"]
        except:
            size = False

        if colour and size:
            item = {"id": product_id, "quantity": 1, "size": size, "colour": colour}
            count = 0
            if bag != []:
                for product in bag:
                    if (
                        product["id"] == product_id
                        and product["size"] == size
                        and product["colour"] == colour
                    ):
                        break
                    else:
                        count += 1
                if count == len(bag):
                    bag.append(item)
                else:
                    bag[count]["quantity"] += 1
            else:
                bag.append(item)
        elif size and not colour:
            item = {"id": product_id, "quantity": 1, "size": size}
            count = 0
            if bag != []:
                for product in bag:
                    if product["id"] == product_id and product["size"] == size:
                        break
                    else:
                        count += 1
                if count == len(bag):
                    bag.append(item)
                else:
                    bag[count]["quantity"] += 1
            else:
                bag.append(item)
        else:
            item = {"id": product_id, "quantity": 1, "colour": colour}
            count = 0
            if bag != []:
                for product in bag:
                    if product["id"] == product_id and product["colour"] == colour:
                        break
                    else:
                        count += 1
                if count == len(bag):
                    bag.append(item)
                else:
                    bag[count]["quantity"] += 1
            else:
                bag.append(item)
        request.session["bag"] = bag
        return redirect(reverse("home"))

    if request.GET:
        bag = request.session.get("bag", [])

        item = {"id": product_id, "quantity": 1}
        count = 0
        for product in bag:
            if product["id"] == item["id"]:
                break
            else:
                count += 1
        if count == len(bag):
            bag.append(item)
        else:
            bag[count]["quantity"] += 1
        request.session["bag"] = bag
        return redirect(reverse("home"))


# Create your views here
def delete_from_bag(request, product_id):
    """A view to delete products from bag"""

    bag = request.session.get("bag", [])

    index = bag.pop(product_id - 1)

    request.session["bag"] = bag

    return redirect(reverse("home"))
