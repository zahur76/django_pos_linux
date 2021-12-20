from django import forms

from .models import Category


class add_categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            "name": "Add Category Name",
        }

        for field in self.fields:
            self.fields[field].widget.attrs["placeholder"] = placeholders[field]
            self.fields[field].widget.attrs[
                "class"
            ] = "border-dark rounded-0 mx-auto add-category-form-input m-1"
            self.fields[field].label = False


class add_subcategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ("category",)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            "name": "Add Subcategory",
        }

        for field in self.fields:
            self.fields[field].widget.attrs["placeholder"] = placeholders[field]
            self.fields[field].widget.attrs[
                "class"
            ] = "border-dark rounded-0 mx-auto add-category-form-input m-1"
            self.fields[field].label = False
