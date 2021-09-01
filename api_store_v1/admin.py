from django.contrib import admin

# Register your models here.
from api_store_v1.models import Store, Product

admin.site.register(Store)
admin.site.register(Product)
