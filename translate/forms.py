from django import forms

from .models import Language


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"
            ] = "border-dark rounded-0 mx-auto add-category-form-input m-1"
            self.fields[field].label = False
