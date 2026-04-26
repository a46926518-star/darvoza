from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Category, Product, Order, Profile, Feedback
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, ProfileSerializer, FeedbackSerializer

# --- KATEGORIYALAR ---
class CategoryListView(generics.ListAPIView):
    """Barcha kategoriyalar ro'yxati"""
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

# --- MAHSULOTLAR ---
class ProductListView(generics.ListAPIView):
    """Barcha mahsulotlar ro'yxati (Filtrlar bilan)"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'id']

class ProductDetailView(generics.RetrieveAPIView):
    """Bitta mahsulot haqida ma'lumot (ID orqali)"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

class ProductSearchView(generics.ListAPIView):
    """Mahsulotlarni nomi bo'yicha qidirish (/search/?q=nomi)"""
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Product.objects.filter(name__icontains=query)

# --- BUYURTMALAR ---
class OrderCreateView(generics.CreateAPIView):
    """Yangi buyurtma berish"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

class OrderListView(generics.ListAPIView):
    """Barcha buyurtmalar ro'yxati (Admin uchun)"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Buyurtmani ko'rish, tahrirlash yoki o'chirish"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

# --- PROFIL VA FEEDBACK ---
class ProfileDetailView(generics.RetrieveUpdateAPIView):
    """Foydalanuvchi profili (Telegram ID orqali)"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'telegram_id'

class FeedbackCreateView(generics.CreateAPIView):
    """Fikr-mulohaza qoldirish"""
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.AllowAny]



class NewProductsView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-id')[:5]
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

class TopProductsView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-price')[:5]
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

class ProductsByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        cat_id = self.kwargs['cat_id']
        return Product.objects.filter(category_id=cat_id)

class OrderStatsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        count = Order.objects.count()
        return Response({"total_orders": count})

class ProfileCreateView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]