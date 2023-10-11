# Insert into single table with many-to-many relationship table

```python
from inventory.models import Product, Category, ProductInventory, Brand, ProductType

ProductInventory.objects.all().delete()
Brand.objects.all().delete()
Product.objects.all().delete()
ProductType.objects.all().delete()
Category.objects.all().delete()

x = Product(web_id='12345',slug='ex1',name='ex1',description='ex1',is_active=True)
x.save()
y = Category(name='Flip-Flops', slug='flipflops', is_active=True)
y.save()

x = Product(web_id='123456780',slug='ex100000',name='ex100000',description='ex10000',is_active=True)
x.save()

x = Product.objects.get(id=3)
y = Category.objects.get(id=42)

x.category.add(Category.objects.get(id=1))

y = Category(name='Flip-Flops2', slug='flipflops2', is_active=True)
y.save()

y = Category.objects.all()
x.category.add(*y)

```
