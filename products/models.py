from django.db import models
import uuid


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)

    # Will return the actual name in admin fields
    def __str__(self):
        return self.name

class subCategory(models.Model):

    class Meta:
        verbose_name_plural = "subCategory"

    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='cat')
    # category.cat.all: will return all subCategory for that specific category

    # Will return the actual name in admin fields
    def __str__(self):
        return self.name

class Product(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL, related_name="prod")
    subcategory = models.ForeignKey('subCategory', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    has_colour = models.BooleanField(default=False, null=True, blank=True)
    stock_available = models.IntegerField()
    has_vat = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """
        Create SKU on save 
        """
        first_sku = self.category
        self.sku = f'{first_sku.name[0]}/{self.subcategory}-'+(uuid.uuid4().hex.upper())[:8]
        super().save(*args, **kwargs)
