from django.urls import path
from .views import (
    CategoryListView,
    ProductListView,
    ProductDetailView,
    ProductSearchView,
    OrderCreateView,
    OrderListView,
    OrderDetailView,
    ProfileDetailView,
    FeedbackCreateView
)

urlpatterns = [
    # Kategoriya
    path('kategoriyalar/', CategoryListView.as_view(), name='category-list'),

    # Mahsulotlar
    path('mahsulotlar/', ProductListView.as_view(), name='product-list'),
    path('mahsulotlar/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('mahsulotlar/search/', ProductSearchView.as_view(), name='product-search'),

    # Buyurtmalar
    path('buyurtma-berish/', OrderCreateView.as_view(), name='order-create'),
    path('buyurtmalar-ruyxati/', OrderListView.as_view(), name='order-list'),
    path('buyurtma/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

    # Profil va Feedback
    path('profile/<int:telegram_id>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback-create'),
]