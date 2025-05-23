from rest_framework import serializers
from .models import Product, Category, Review
from rest_framework.exceptions import ValidationError


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
        fields = 'text', 'stars', 'product_id'


class ProductsReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = 'title', 'reviews', 'rating'


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=2, max_length=256)
    description = serializers.CharField(required=True, min_length=1)
    price = serializers.FloatField(required=True)
    is_active = serializers.BooleanField(required=True)
    category_id = serializers.IntegerField(required=True, min_value=1)

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except:
            raise ValidationError('Category does not exist')
        return category_id


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=1, max_length=256)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, min_length=1, max_length=256)
    stars = serializers.IntegerField(required=True, min_value=1, max_value=5)
    product_id = serializers.IntegerField(required=True, min_value=1)

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except:
            raise ValidationError('Product does not exist')
        return product_id