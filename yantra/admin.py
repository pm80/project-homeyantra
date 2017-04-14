from django.contrib import admin

# Register your models here.
from .models import  Hisab

class ProductAdmin(admin.ModelAdmin):
    list_display = ['p_id','p_name','p_type', 'price', 'quantity', 'image']
    list_filter = ['p_type']
    search_fields = ['p_id', 'p_name']


#admin.site.register(Product, ProductAdmin)
admin.site.register(Hisab)


