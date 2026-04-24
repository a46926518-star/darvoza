from django.urls import path
from .views import (
    CategoryListView,
    ProductListView,
    ProductDetailView,
    OrderCreateView
)

urlpatterns = [
    path('kategoriyalar/', CategoryListView.as_view(), name='category-list'),

    path('mahsulotlar/', ProductListView.as_view(), name='product-list'),
    path('mahsulotlar/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('buyurtma/', OrderCreateView.as_view(), name='order-create'),
]