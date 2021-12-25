from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import  Language
from .forms import LanguageForm
from django.contrib import messages


# Create your views here
def translate(request):
    """A view to change Language """

    form = LanguageForm()

    my_language = request.session['my_language']

    if request.POST:
            my_language['language'] = request.POST['name']
    request.session['my_language'] = my_language

    context = {
        'language': my_language,
        'form': form,
    }

    return render(request, "translate/translate.html", context)

