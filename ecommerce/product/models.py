from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=20)
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True
    )  # managing subcategory

    class MPTTMeta:
        order_insertion_by = ["name"]


    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    digital = models.BooleanField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey("Category",blank=True,null=True, on_delete=models.SET_NULL)
    def __str__(self) -> str:
        return self.name
