from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import (ProductDetailSerializer,
                          ProductListSerializer,
                          CategorySerializer,
                          ReviewSerializer,
                          ProductsReviewsSerializer)


@api_view(['GET'])
def product_detail_api_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(product, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)



@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.filter(is_active=True)
    data = ProductListSerializer(products, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_detail_api_view(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = CategorySerializer(category, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    data = CategorySerializer(categories, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_api_view(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def products_reviews_api_view(request):
    products = Product.objects.all()
    data = ProductsReviewsSerializer(products, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)