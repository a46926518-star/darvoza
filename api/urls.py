from django.urls import path
from .views import  CategoryListView,ProductListView, ProductDetailView,OrderCreateView,ProfileDetailView, FeedbackCreateView






urlpatterns = [
    path('kategoriyalar/', CategoryListView.as_view(), name='category-list'),
    path('mahsulotlar/', ProductListView.as_view(), name='product-list'),
    path('mahsulotlar/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('buyurtma/', OrderCreateView.as_view(), name='order-create'),
    path('profile/<int:telegram_id>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback-create'),
]