from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here
def admin_center(request):
    """A view to return the index page"""

    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    return render(request, "admin_center/admin_center.html")

