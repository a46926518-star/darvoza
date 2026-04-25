from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Category, Product, Order, Profile, Feedback
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer,ProfileSerializer, FeedbackSerializer

class CategoryListView(generics.ListAPIView):
    """Kategoriyalar ro'yxatini olish"""
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class ProductListView(generics.ListAPIView):
    """Mahsulotlar ro'yxatini filtrlash va qidirish bilan olish"""
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'id']

    def get_queryset(self):
        return Product.objects.all()

class ProductDetailView(generics.RetrieveAPIView):
    """Bitta mahsulot haqida batafsil ma'lumot olish"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

class OrderCreateView(generics.CreateAPIView):
    """Yangi buyurtma yaratish"""
    # Mana shu yerda 'objects' to'g'ri yozildi:
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                {
                    "status": "success",
                    "message": "Buyurtma qabul qilindi!",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "status": "error",
                "message": "Ma'lumotlar xato yuborildi",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class ProfileDetailView(generics.RetrieveUpdateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'telegram_id' # URL'da id o'rniga telegram_id ishlatamiz

class FeedbackCreateView(generics.CreateAPIView):

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.AllowAny]