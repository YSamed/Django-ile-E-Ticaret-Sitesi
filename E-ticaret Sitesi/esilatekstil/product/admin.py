from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin
from .models import Category, Product, Images

# Ürün resimlerini içeren içerik
class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 5

# Kategori admin paneli
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'gender', 'image_display']
    list_filter = ['gender']
    readonly_fields = ('image_display',)

    # Resim gösterimini sağlayan fonksiyon
    def image_display(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" height="50"/>'.format(obj.image.url))
        else:
            return 'Resim yok'

    image_display.short_description = 'Resim'

# Ürün admin paneli
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'amount', 'image_display', 'gender']
    readonly_fields = ('image_display',)

    # Resim gösterimini sağlayan fonksiyon
    def image_display(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" height="50"/>'.format(obj.image.url))
        else:
            return 'Resim yok'

    image_display.short_description = 'Resim'

# Resim admin paneli
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'image_tag']
    readonly_fields = ('image_tag',)

# Kategori admin paneli için özel ayarlar
class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Kumulatif ürün sayısını ekleyin
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Kumulatif olmayan ürün sayısını ekleyin
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count + instance.products_cumulative_count

    related_products_count.short_description = 'İlgili ürünler'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = 'İlgili ürünler (ağaç içinde)'

# Admin paneline kayıt et
admin.site.register(Category, CategoryAdmin2)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)
