from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import add_categoryForm, add_productForm, add_subcategoryForm
from .models import Category, Product, subCategory


# Create your views here
def category(request):
    """A view Category Management"""

    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = add_categoryForm(request.POST)
        if form.is_valid():
            try:
                print(request.POST["name"].lower())
                category = get_object_or_404(
                    Category, name=request.POST["name"].lower()
                )
                messages.error(request, "Category Already Exists!")
                return redirect(reverse("category"))
            except:
                new_form = form.save(commit=False)
                new_form.name = request.POST["name"].lower()
                new_form.save()
                messages.success(request, "Category Added!")
                return redirect(reverse("category"))
        messages.error(request, "Error, Please try again!")

    categories = Category.objects.all()

    form = add_categoryForm()

    context = {
        "categories": categories,
        "form": form,
    }

    return render(request, "products/category.html", context)


def category_delete(request, category_id):
    """A view to delete category"""

    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    category = get_object_or_404(Category, id=category_id)

    category.delete()
    messages.success(request, "Category Deleted!")
    return redirect(reverse("category"))


def category_edit(request, category_id):
    """A view to delete category"""

    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = add_categoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Updated!")
            return redirect(reverse("category"))
        messages.error(request, "Error, Please try again!")
    else:
        form = add_categoryForm(instance=category)

        context = {
            "category": category,
            "form": form,
        }

        return render(request, "products/edit_category.html", context)


def subcategory(request):
    """A view Subcategory Management"""

    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    categories = Category.objects.all()

    context = {
        "categories": categories,
    }

    return render(request, "products/subcategory.html", context)


def add_subcategory(request, category_name):
    """A view to add Subcategory"""

    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    category = get_object_or_404(Category, name=category_name)

    if request.method == "POST":
        category = get_object_or_404(Category, name=category_name)
        name = request.POST["name"].lower()
        try:
            check_subcategory = get_object_or_404(
                subCategory, name=name, category=category
            )
            messages.error(request, "Subcategory already exists!")
            return redirect(reverse("subcategory"))
        except:
            subcategory = subCategory.objects.create(name=name, category=category)
            messages.success(request, "Subcategory Added!")
            return redirect(reverse("subcategory"))
    form = add_subcategoryForm()
    context = {
        "category": category,
        "form": form,
    }

    return render(request, "products/add_subcategory.html", context)


def delete_subcategory(request, subcategory_id):
    """A view to delete Subcategory"""
    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    subcategory = get_object_or_404(subCategory, id=subcategory_id)
    subcategory.delete()
    messages.success(request, "Subcategory Deleted!")
    return redirect(reverse("subcategory"))


def edit_subcategory(request, subcategory_id):
    """A view to edit Subcategory"""
    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    subcategory = get_object_or_404(subCategory, id=subcategory_id)
    if request.method == "POST":
        form = add_subcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.name = request.POST["name"].lower()
            new_form.save()
            messages.success(request, "Subcategory Updated!")
            return redirect(reverse("subcategory"))
        messages.error(request, "Error, Please try again!")

    form = add_categoryForm(instance=subcategory)

    context = {
        "form": form,
        "subcategory": subcategory,
    }

    return render(request, "products/edit_subcategory.html", context)


def products(request):
    """A view to Manage products"""

    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    if "q" in request.GET:
        query = request.GET["q"]
        if not query:
            return redirect(reverse("products"))
        else:
            all_products = Product.objects.all()
            queries = Q(name__icontains=query) | Q(category__name__icontains=query)
            query_products = all_products.filter(queries)
            context = {
                "products": query_products,
            }
            return render(request, "products/products.html", context)

    categories = Category.objects.all()

    products = Product.objects.all()

    context = {
        "products": products,
        "categories": categories,
    }

    return render(request, "products/products.html", context)


def add_product(request, category_id):
    """A view add Product"""

    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    category = get_object_or_404(Category, id=category_id)

    if request.method == "POST":
        form = add_productForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.category = category
            new_form.save()
            messages.success(request, "Product added!")
            return redirect(reverse("products"))
        messages.error(request, "Error, try again!")
        return redirect(reverse("products"))

    form = add_productForm()

    context = {
        "form": form,
        "category": category,
    }

    return render(request, "products/add_product.html", context)


def delete_product(request, product_id):
    """A view to delete Subcategory"""
    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, "Product Deleted!")
    return redirect(reverse("products"))


def update_product(request, product_id):
    """A view to delete Subcategory"""
    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, id=product_id)
    category = get_object_or_404(Category, id=product.category.id)

    if request.method == "POST":
        form = add_productForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.category = category
            new_form.save()
            messages.success(request, "Product updated!")
            return redirect(reverse("products"))
        messages.error(request, "Error, try again!")
        return redirect(reverse("products"))

    form = add_productForm(instance=product)

    context = {
        "product": product,
        "form": form,
        "category": category,
    }
    return render(request, "products/update_product.html", context)
