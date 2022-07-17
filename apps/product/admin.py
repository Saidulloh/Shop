from django.contrib import admin
from .models import *
# Register your models here
from mptt.admin import DraggableMPTTAdmin

admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),  
    prepopulated_fields = {'slug':['title']},
)


class ProductImageInLine(admin.TabularInline):
    model = Images
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'price', 'image_tag')
    list_filter = ['category']
    prepopulated_fields = {'slug':['title']}
    inlines = [ProductImageInLine]

admin.site.register(Product, ProductAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image_tag']

admin.site.register(Images, ImageAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'product', 'created')
    search_fields = ('name', 'email', 'review')
admin.site.register(Review, ReviewAdmin)