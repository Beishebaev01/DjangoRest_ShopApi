from django.urls import path
from product import views

urlpatterns = [
    path('', views.product_list_create_api_view),
    path('<int:product_id>/', views.product_detail_api_view),
    path('categories/', views.category_list_create_api_view),
    path('categories/<int:category_id>/', views.category_detail_api_view),
    path('reviews/', views.review_list_create_api_view),
    path('reviews/<int:review_id>/', views.review_detail_api_view),
    path('product_reviews/', views.products_reviews_api_view)
]