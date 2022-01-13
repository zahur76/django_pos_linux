from django import forms

from .models import Category, Product, subCategory


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
        model = subCategory
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


class add_productForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = (
            "sku",
            "category",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            "name": "Name",
            "has_sizes": "Size Present",
            "sizes_available": "Enter Sizes",
            "colour_available": "Enter Colours",
            "has_colour": "Colour Present",
            "has_vat": "Vat Article",
            "stock_available": "Stock",
            "image": "Image",
            "price": "Price",
        }

        self.fields["subcategory"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "category" and field != "subcategory":
                self.fields[field].widget.attrs["placeholder"] = placeholders[field]
            self.fields[field].widget.attrs[
                "class"
            ] = "border-dark rounded-0 add-product-form-input m-1"
            if field not in [
                "has_sizes",
                "has_vat",
                "has_colour",
                "sizes_available",
                "colour_available",
            ]:
                self.fields[field].label = False
