from django.urls import path
from . import views

urlpatterns = [
    # Kategoriya yo'llari
    path('kategoriyalar/', views.CategoryListView.as_view(), name='category-list'),
    path('kategoriyalar/<int:cat_id>/mahsulotlar/', views.ProductsByCategoryView.as_view(), name='category-products'),

    # Mahsulot yo'llari
    path('mahsulotlar/', views.ProductListView.as_view(), name='product-list'),
    path('mahsulotlar/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('mahsulotlar/search/', views.ProductSearchView.as_view(), name='product-search'),
    path('mahsulotlar/yangi/', views.NewProductsView.as_view(), name='product-new'),
    path('mahsulotlar/top/', views.TopProductsView.as_view(), name='product-top'),

    # Buyurtma yo'llari
    path('buyurtma-berish/', views.OrderCreateView.as_view(), name='order-create'),
    path('buyurtmalar-ruyxati/', views.OrderListView.as_view(), name='order-list'),
    path('buyurtma/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('statistika/', views.OrderStatsView.as_view(), name='order-stats'),

    # Profil va Feedback
    path('profile/yaratish/', views.ProfileCreateView.as_view(), name='profile-create'),
    path('profile/<int:telegram_id>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('feedback/', views.FeedbackCreateView.as_view(), name='feedback-create'),
]