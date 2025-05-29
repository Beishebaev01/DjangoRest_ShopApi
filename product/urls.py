from django.urls import path
from product import views
from utils.constants import LIST_CREATE, REVIEW_UPDATE_DESTROY

urlpatterns = [
    path('', views.ProductViewSet.as_view(LIST_CREATE)),
    path('<int:id>/', views.ProductViewSet.as_view(REVIEW_UPDATE_DESTROY)),
    path('categories/', views.CategoryViewSet.as_view(LIST_CREATE)),
    path('categories/<int:id>/', views.CategoryViewSet.as_view(REVIEW_UPDATE_DESTROY)),
    path('reviews/', views.ReviewAPIViewSet.as_view(LIST_CREATE)),
    path('reviews/<int:id>/', views.ReviewAPIViewSet.as_view(REVIEW_UPDATE_DESTROY)),
    path('product_reviews/', views.ProductReviewsListAPIView.as_view()),
]