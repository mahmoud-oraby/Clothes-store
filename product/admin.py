from django.contrib import admin
from .models import Product, Color, Size, Currency
# Register your models here.

admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Currency)
