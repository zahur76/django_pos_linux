import uuid

from django.db import models

# Create your models here.


class Order(models.Model):
    class Meta:
        verbose_name_plural = "Orders"

    order_number = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    net_total = models.IntegerField()
    vat = models.IntegerField()
    gross_total = models.IntegerField()

    # Will return the actual name in admin fields
    def __str__(self):
        return self.order_number

    def save(self, *args, **kwargs):
        """
        Create Order Number on save
        """
        self.sku = uuid.uuid4().hex.upper()
        super().save(*args, **kwargs)


class Order(models.Model):
    class Meta:
        verbose_name_plural = "Orders"

    order_number = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    net_total = models.DecimalField(max_digits=6, decimal_places=2)
    vat = models.DecimalField(max_digits=6, decimal_places=2)
    gross_total = models.DecimalField(max_digits=6, decimal_places=2)

    # Will return the actual name in admin fields
    def __str__(self):
        return self.order_number

    def save(self, *args, **kwargs):
        """
        Create Order Number on save
        """
        self.order_number = uuid.uuid4().hex.upper()
        super().save(*args, **kwargs)


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    product = product = models.ForeignKey(
        "products.Product", null=False, blank=False, on_delete=models.CASCADE
    )
    size = models.CharField(max_length=254, null=False, blank=False, default="none")
    colour = models.CharField(max_length=254, null=False, blank=False, default="none")
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2)
    lineItem_vat = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.order.order_number}"
