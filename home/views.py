from django.db.models import Q
from django.shortcuts import redirect, render, reverse

from products.models import Category, Product, subCategory


# Create your views here
def index(request):
    """A view to return the index page"""

    try:
        request.session["my_language"]
    except:
        request.session["my_language"] = {"language": "en"}

    all_products = Product.objects.all()
    all_categories = Category.objects.all()

    if request.POST:
        query = request.POST["q"]
        if not query:
            return redirect(reverse("home"))
        else:
            queries = Q(name__icontains=query)
            query_product = all_products.filter(queries)
            context = {
                "products": query_product,
                "categories": all_categories,
            }
            return render(request, "home/index.html", context)

    if "All" in request.GET:

        context = {
            "products": all_products,
            "categories": all_categories,
        }

        return render(request, "home/index.html", context)

    if "query" in request.GET:
        query = request.GET.getlist("query")

        if len(query) == 1:

            query_product = Product.objects.filter(category__name=query[0])

            context = {
                "query": query,
                "products": query_product,
                "categories": all_categories,
            }
            return render(request, "home/index.html", context)

        query_product = Product.objects.filter(
            category__name=query[0], subcategory__name=query[1]
        )

        context = {
            "query": query,
            "products": query_product,
            "categories": all_categories,
        }

        return render(request, "home/index.html", context)

    context = {
        "products": all_products,
        "categories": all_categories,
    }

    return render(request, "home/index.html", context)
