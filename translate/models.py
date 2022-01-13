from django.db import models

languages = (
    (None, "Choose Language"),
    ("en", "en"),
    ("fr", "fr"),
)


class Language(models.Model):
    class Meta:
        verbose_name_plural = "Languages"

    name = models.CharField(max_length=254, choices=languages)

    # Will return the actual name in admin fields
    def __str__(self):
        return self.name
