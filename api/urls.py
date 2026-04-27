from django.urls import path
from . import views

urlpatterns = [
    path('kategoriyalar/', views.CategoryListView.as_view(), name='category-list'),
    path('mahsulotlar/', views.ProductListView.as_view(), name='product-list'),
    path('mahsulotlar/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    path('kategoriyalar/mahsulotlar/', views.ProductListView.as_view()),
    path('mahsulotlar/search/', views.ProductListView.as_view()),

    path('buyurtma-berish/', views.OrderCreateView.as_view(), name='order-create'),
    path('profil/<int:telegram_id>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('feedback/', views.FeedbackCreateView.as_view(), name='feedback-create'),

    path('admin/kategoriya-qushish/', views.CategoryCreateView.as_view()),
    path('admin/mahsulot-qushish/', views.ProductCreateView.as_view()),
    path('admin/mahsulot-tahrirlash/<int:pk>/', views.ProductUpdateDeleteView.as_view()),

    path('cart/', views.CartListView.as_view(), name='cart-list'),
    path('cart/add/', views.CartAddView.as_view(), name='cart-add'),
]