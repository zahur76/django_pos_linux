from django.shortcuts import render


# Create your views here
def admin_center(request):
    """A view to return the index page"""

    return render(request, "admin_center/admin_center.html")

