from django.contrib import admin

from .models import Product, Category, ProductImage
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {
        'slug': ('name',)
        }


admin.site.register(Category, CategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'price', 'discounted_price', 'in_stock', 'is_active', 'created_at']
    prepopulated_fields = {
        'slug': ('title',)
        }
    list_editable = ['discounted_price', 'in_stock', 'is_active']
    list_filter = ['category', 'is_active', 'in_stock', 'created_at']
    # list_display_links = ['category']


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)