from django.db import models


class Language(models.Model):
    class Meta:
        verbose_name_plural = "Languages"

    name = models.CharField(max_length=254)

    # Will return the actual name in admin fields
    def __str__(self):
        return self.name


class activeLanguage(models.Model):
    class Meta:
        verbose_name_plural = "active language"

    language= models.ForeignKey(
        "Language", null=True, blank=True, on_delete=models.SET_NULL, related_name="lang"
    )

    # Will return the actual name in admin fields
    def __str__(self):
        return self.language.name