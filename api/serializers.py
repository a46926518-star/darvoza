import requests
from rest_framework import serializers
from .models import Category, Product, Order, OrderItem, Comment,Profile,Feedback,CartItem
from django.contrib.auth.models import User


def send_telegram_admin(order_id, phone, full_name, total_price):
    token = "6821360156:AAEmr6l7_h6lM1f3p3L-l_l_l_l_l"
    admin_id = "8549599284"
    text = (
        f"🔔 Yangi buyurtma keldi!\n\n"
        f"🆔 ID: {order_id}\n"
        f"👤 Mijoz: {full_name}\n"
        f"📞 Tel: {phone}\n"
        f"💰 Jami: {total_price} $\n\n"
        f"🔗 Batafsil: https://darvoza-bot-service.onrender.com/admin/"
    )

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        requests.post(url, data={'chat_id': admin_id, 'text': text})
    except Exception as e:
        print(f"Xabar yuborishda xatolik: {e}")




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order = super().create(validated_data)

        send_telegram_admin(
            order_id=order.id,
            phone=order.phone_number,
            full_name=order.full_name,
            total_price=order.total_amount
        )

        return order


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = ['id', 'username', 'telegram_id', 'phone_number', 'address']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'subject', 'message', 'created_at']



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user




class CartItemSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_details', 'quantity']