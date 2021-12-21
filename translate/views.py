from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import activeLanguage, Language
from .forms import add_activeLanguageForm
from django.contrib import messages


# Create your views here
def translate(request):
    """A view change Language """

    active_language = get_object_or_404(activeLanguage)

    form = add_activeLanguageForm(instance=active_language)

    if request.method == "POST":
        form = add_activeLanguageForm(request.POST, instance=active_language)
        if form.is_valid():
            form.save()
            messages.success(request, "Language Updated!")
            return redirect(reverse("admin_center"))
    context = {
        'active_language': active_language,
        'form': form,
    }

    return render(request, "translate/translate.html", context)


def change_language(request):
    """A view to change Language """

    if request.method == "GET":
        active_language = get_object_or_404(activeLanguage)

        language = get_object_or_404(Language, name=request.GET['language'])

        active_language.language = language
        active_language.save()
        messages.success(request, "Language Updated!")
        return redirect(reverse("home"))
