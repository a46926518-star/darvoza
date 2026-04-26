from django.urls import path
from .views import (
    # Eskilar
    CategoryListView,
    ProductListView,
    ProductDetailView,
    ProductSearchView,
    OrderCreateView,
    OrderListView,
    OrderDetailView,
    ProfileDetailView,
    FeedbackCreateView,
    # Yangi qo'shilgan 5 tasi
    NewProductsView,
    TopProductsView,
    ProductsByCategoryView,
    OrderStatsView,
    ProfileCreateView
)

urlpatterns = [
    # --- Kategoriya ---
    path('kategoriyalar/', CategoryListView.as_view(), name='category-list'),
    path('kategoriyalar/<int:cat_id>/mahsulotlar/', ProductsByCategoryView.as_view(), name='category-products'),

    # --- Mahsulotlar ---
    path('mahsulotlar/', ProductListView.as_view(), name='product-list'),
    path('mahsulotlar/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('mahsulotlar/search/', ProductSearchView.as_view(), name='product-search'),
    path('mahsulotlar/yangi/', NewProductsView.as_view(), name='product-new'),
    path('mahsulotlar/top/', TopProductsView.as_view(), name='product-top'),

    # --- Buyurtmalar ---
    path('buyurtma-berish/', OrderCreateView.as_view(), name='order-create'),
    path('buyurtmalar-ruyxati/', OrderListView.as_view(), name='order-list'),
    path('buyurtma/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('statistika/', OrderStatsView.as_view(), name='order-stats'),

    # --- Profil va Feedback ---
    path('profile/yaratish/', ProfileCreateView.as_view(), name='profile-create'),
    path('profile/<int:telegram_id>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback-create'),
]