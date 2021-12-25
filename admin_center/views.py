from django.contrib import messages
from django.shortcuts import redirect, render, reverse


# Create your views here
def admin_center(request):
    """A view to return the index page"""
    
    my_language = request.session['my_language']
    print(my_language)

    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    return render(request, "admin_center/admin_center.html")
