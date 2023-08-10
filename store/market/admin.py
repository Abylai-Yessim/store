from django.contrib import admin
from .models import Product
from .models import Busket
from .models import Fields
# Register your models here.
# admin.site.register(Product)
# admin.site.register(Busket)
admin.site.register(Fields)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title', 'text')
    
@admin.register(Busket)
class BusketAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title', 'text')

