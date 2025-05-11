from rest_framework import serializers
from .models import Product, Category, Review


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id', 'title', 'price', 'category', 'reviews'
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    product_count = ProductListSerializer
    class Meta:
        model = Category
        fields = 'name', 'product_count'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text', 'stars'


class ProductsReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = 'title', 'reviews', 'rating'