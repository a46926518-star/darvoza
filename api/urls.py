from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('kategoriyalar/', views.CategoryListView.as_view(), name='category-list'),
    path('admin/kategoriya-qushish/', views.CategoryCreateView.as_view(), name='category-create'),


    path('mahsulotlar/', views.ProductListView.as_view(), name='product-list'),
    path('mahsulotlar/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('admin/mahsulot-qushish/', views.ProductCreateView.as_view(), name='product-create'),
    path('admin/mahsulot-tahrirlash/<int:pk>/', views.ProductUpdateDeleteView.as_view(), name='product-update-delete'),


    path('buyurtma-berish/', views.OrderCreateView.as_view(), name='order-create'),


    path('cart/', views.CartListView.as_view(), name='cart-list'),
    path('cart/add/', views.CartAddView.as_view(), name='cart-add'),

    # Profil & Feedback
    path('profil/<int:telegram_id>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('feedback/', views.FeedbackCreateView.as_view(), name='feedback-create'),
]