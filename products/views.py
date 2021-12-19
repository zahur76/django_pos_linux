from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import Category, subCategory
from .forms import add_categoryForm, add_subcategoryForm
from django.contrib import messages

# Create your views here
def category(request):
    """A view Category Management"""

    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = add_categoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Added!")
            return redirect(reverse("category"))
        messages.error(request, "Error, Please try again!")

    categories = Category.objects.all()

    form = add_categoryForm()        

    context = {
        'categories': categories,
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
            'category': category,
            'form': form,
        }

        return render(request, "products/edit_category.html", context)


def subcategory(request):
    """A view Subcategory Management"""

    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    categories = Category.objects.all()      

    context = {
        'categories': categories,
        
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
        name = request.POST['name']
        subcategory = subCategory.objects.create(
            name=name,
            category=category
        )       
        return redirect(reverse("subcategory"))
    form = add_subcategoryForm()
    context = {
        'category': category,
        'form': form,
    }

    return render(request, "products/add_subcategory.html", context)


def delete_subcategory(request, subcategory_id):
    """A view to delete Subcategory"""

    subcategory = get_object_or_404(subCategory, id=subcategory_id)
    subcategory.delete()
    messages.success(request, "Subcategory Deleted!")
    return redirect(reverse("subcategory"))


def edit_subcategory(request, subcategory_id):
    """A view to edit Subcategory"""

    subcategory = get_object_or_404(subCategory, id=subcategory_id)
    if request.method == "POST":
        form = add_subcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            messages.success(request, "Subcategory Updated!")
            return redirect(reverse("subcategory"))
        messages.error(request, "Error, Please try again!")
    
    
    form = add_categoryForm(instance=subcategory)

    context = {
        'form': form,
        'subcategory': subcategory,
    }

    return render(request, "products/edit_subcategory.html", context)
    
    