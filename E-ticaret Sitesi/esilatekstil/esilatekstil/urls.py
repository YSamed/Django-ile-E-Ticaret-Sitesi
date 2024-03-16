from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from homeapp import views
from order import views as orderviews

urlpatterns = [
    # Admin paneli URL'si
    path('admin/', admin.site.urls),
    
    # Ana sayfa URL'si
    path('anasayfa/', views.index, name='index'),

    # Ürünler URL'si
    path('ürünler/', views.products, name='products'),

    # Sepet URL'si
    path('sepet/', orderviews.shopcart, name='shopcart'),
    
    # Sepete ürün eklemek için URL'si (düzeltildi)
    path('order/addtocart/<int:product_id>/', orderviews.add_to_cart, name='add_to_cart'),
    
    # Kategoriye özgü ürünler URL'si
    path('category/<int:id>/<slug:slug>/', views.category_products, name='category_products'),
    
    # Django varsayılan kimlik doğrulama URL'lerini kullanmak için prefix
    path("accounts/", include('django.contrib.auth.urls')),
    
    # 'homeapp' uygulamasının URL'lerini dahil et
    path("", include('homeapp.urls')),
    
    # 'product' uygulamasının URL'lerini dahil et
    path("products/", include('product.urls')),
    
    # Ürün detayı URL'si
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    
    # Ürün arama URL'si
    path('search/', views.product_search, name='product_search'),
    
    # Otomatik ürün arama URL'si
    path('search_auto/', views.product_search_auto, name='product_search_auto'),

    # Kayıt URL'si
    
    path('signup/', views.signup_view, name='signup'),

    # Giriş URL'si
    path('login/', views.login_view, name='login_view'),

    # Çıkış URL'si
    path('logout/', views.logout_view, name='logout_view'),

    # Anasayfa URL'si (Boş URL)
    path('', TemplateView.as_view(template_name='anasayfa.html'), name='anasayfa'),

    path('order/', include('order.urls')),
    
]

# DEBUG modunda ise, medya dosyaları için static URL'yi ekleyin
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
