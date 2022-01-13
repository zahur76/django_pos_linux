from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import LanguageForm


# Create your views here
def translate(request):
    """A view to change Language"""

    if not request.user.is_superuser:
        messages.error(request, "Permision Denied!.")
        return redirect(reverse("home"))

    my_language = request.session["my_language"]
    form = LanguageForm()

    if request.POST:
        my_language["language"] = request.POST["name"]
        request.session["my_language"] = my_language

        messages.success(request, "Language Changed!.")
        return redirect(reverse("admin_center"))

    context = {
        "language": my_language,
        "form": form,
    }

    return render(request, "translate/translate.html", context)


# Create your views here
def menu_language(request):
    """A view to change Language on navbar"""

    my_language = request.session["my_language"]

    if request.GET:
        print(request.GET["lang"])
        my_language["language"] = request.GET["lang"]
        request.session["my_language"] = my_language

        messages.success(request, "Language Changed!.")
        return redirect(reverse("admin_center"))
