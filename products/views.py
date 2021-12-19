from django.shortcuts import render
from .models import Category


# Create your views here
def category(request):
    """A view to return the index page"""

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, "products/category.html", context)
