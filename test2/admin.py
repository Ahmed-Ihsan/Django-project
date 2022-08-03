from django.contrib import admin

# Register your models here.
from .models import item ,sales

admin.site.register(item)
admin.site.register(sales)
