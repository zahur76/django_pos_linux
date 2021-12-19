from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import Category
from .forms import add_categoryForm
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
    
    