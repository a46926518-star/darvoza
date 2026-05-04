from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    html_content = """
    <h1>Darvoza API </h1>
    <p>Mavjud ochiq yo'llar:</p>
    <ul>
        <li><a href="/api/mahsulotlar/">/api/mahsulotlar/</a> - Mahsulotlar ro'yxati</li>
        <li><a href="/api/kategoriyalar/">/api/kategoriyalar/</a> - Kategoriyalar</li>
        <li><a href="/cart/">/cart/</a> - Savatcha</li>
        <li><a href="/admin/">/admin/</a> - Boshqaruv paneli</li>
    </ul>
    """
    return HttpResponse(html_content)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    path('', home_view),
]