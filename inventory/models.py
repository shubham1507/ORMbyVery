from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, blank="")

    def __str__(self) -> str:
        return f"Category Name:{self.name}"

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):

    name = models.CharField("Product Name",max_length=100, blank=True)
    age = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    #category = models.ForeignKey(Category,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return f"Product Name:{self.name}"
    class Meta:
        ordering =["age"]

class Stock(models.Model):
    units = models.BigIntegerField()
    Product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Stock Name:{self.Product}"

class Brand(models.Model):

    name = models.CharField(max_length=100)
    brand_id = models.BigAutoField(primary_key=True)

    


    