from django.http import HttpResponse
from .models import Brand,ProductInventory, Stock
from django.db import IntegrityError,transaction

# Create your views here.

def new(request):
    try:
         Brand.objects.create(brand_id = 200, name= 'sparx')

    except IntegrityError:
         return HttpResponse("we can not add")

   
    return HttpResponse("Ram Ram")


def example(request):

    try:
        with transaction.atomic():
            ProductInventory.objects.create(sku='1234',upc='1234',product_type_id=3,product_id=11,brand_id=1, retail_price='10.00', store_price='10.00', sale_price='10.00', weight='100')

            #Stock.objects.create(product_inventory_id=6,units=100)
    except IntegrityError:
        return HttpResponse("Error")

    return HttpResponse("Hi")