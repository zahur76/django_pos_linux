from .models import activeLanguage, Language
from django.shortcuts import get_object_or_404


def active_language(request):
    '''View which shows active language across all apps'''

    active = get_object_or_404(activeLanguage)
    all_languages = Language.objects.all()

    context = {
        'languages': all_languages,
        'active': active,
    }

    return context