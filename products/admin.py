from django.contrib import admin
from .models  import Category, Subcategory, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Category, CategoryAdmin)


class SubcategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Subcategory, SubcategoryAdmin)