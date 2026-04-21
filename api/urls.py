from django.urls import path
from .views import (
    CategoryListView,
    ProductListView,
    ProductDetailView,
    OrderCreateView
)

urlpatterns = [
    # Kategoriyalar ro'yxati: /api/kategoriyalar/
    path('kategoriyalar/', CategoryListView.as_view(), name='category-list'),

    # Mahsulotlar ro'yxati (kategoriya bo'yicha filter bilan): /api/mahsulotlar/
    path('mahsulotlar/', ProductListView.as_view(), name='product-list'),

    # Bitta mahsulot haqida to'liq ma'lumot: /api/mahsulotlar/5/
    path('mahsulotlar/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Buyurtma berish: /api/buyurtma/
    path('buyurtma/', OrderCreateView.as_view(), name='order-create'),
]

