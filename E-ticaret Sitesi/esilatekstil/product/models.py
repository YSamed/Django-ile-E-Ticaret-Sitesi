from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

# Kategori modeli
class Category(MPTTModel):
    # Cinsiyet seçenekleri
    GENDER_CHOICES = (
        ('erkek', 'Erkek'),
        ('kadın', 'Kadın'),
        ('çocuk', 'Çocuk'),
    )
    # Alanlar
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    slug = models.SlugField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    # Ağaç düzeni için sıralama
    class MPTTMeta:
        order_insertion_by = ['title']

    # Kategori adı ve üst kategorileri
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    # Resim görüntüleme
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Resim'


# Ürün modeli
class Product(models.Model):
    # Cinsiyet seçenekleri
    GENDER_CHOICES = (
        ('erkek', 'Erkek'),
        ('kadın', 'Kadın'),
        ('çocuk', 'Çocuk'),
    )
    # Alanlar
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    price = models.FloatField(blank=True)
    amount = models.FloatField()
    detail = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Ürün adı
    def __str__(self):
        return self.title
    

    # Resim görüntüleme
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Resim'


# Ürün resimleri modeli
class Images(models.Model):
    # Alanlar
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    # Resim adı
    def __str__(self):
        return self.title

    # Resim görüntüleme
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Resim'


# Yorum modeli
class Comment(models.Model):
    # Durum seçenekleri
    STATUS = (
        (True, 'Evet'),
        (False, 'Hayır'),
    )
    # Alanlar
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subject = models.CharField(blank=True, max_length=50)
    comment = models.CharField(blank=True, max_length=255)
    rate = models.IntegerField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # Yorum adı
    def __str__(self):
        return self.subject  # veya self.comment
