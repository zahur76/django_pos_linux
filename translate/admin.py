from django.contrib import admin

from .models import Language, activeLanguage


# The model followed by class name (model, class name)
admin.site.register(Language)
admin.site.register(activeLanguage)


