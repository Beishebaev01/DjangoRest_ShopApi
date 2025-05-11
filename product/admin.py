from django.contrib import admin
from .models import Product, Category, Review


class ReviewInline(admin.StackedInline):
    model = Review
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [ReviewInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)