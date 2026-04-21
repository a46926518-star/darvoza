from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Product


class APITests(APITestCase):
    def setUp(self):
        # Test uchun kategoriya yaratish
        self.category = Category.objects.create(name="Test Kategoriya")
        # Test uchun mahsulot yaratish
        self.product = Product.objects.create(
            name="Test Mahsulot",
            price=100.00,
            category=self.category
        )

    def test_get_categories(self):
        """Kategoriyalar ro'yxatini olishni tekshirish"""
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_products(self):
        """Mahsulotlar ro'yxatini olishni tekshirish"""
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


from django.test import TestCase

# Create your tests here.
