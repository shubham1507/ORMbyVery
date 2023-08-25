from django.http import HttpResponse
from .models import Brand
from django.db import IntegrityError

# Create your views here.

def new(request):
    try:
         Brand.objects.create(brand_id = 200, name= 'sparx')

    except IntegrityError:
         return HttpResponse("we can not add")

   
    return HttpResponse("Ram Ram")