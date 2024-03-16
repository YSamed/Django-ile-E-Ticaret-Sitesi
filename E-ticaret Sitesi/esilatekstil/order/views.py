from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from order.models import ShopCart, ShopCartForm
from product.models import Category

# Ana sayfa görüntüsü
def index(request):
    return HttpResponse("Product Page")

# Kullanıcı girişi , ürünü sepete ekleme 
@login_required(login_url='/login')
def addtocart(request, id):
    url = request.META.get('HTTP_REFERER')  # Kullanıcıyı yönlendireceğimiz URL'yi alırız
    current_user = request.user  # Mevcut kullanıcıyı alırız

    # Ürün zaten sepette mi kontrolü
    product_exists = ShopCart.objects.filter(product_id=id, user_id=current_user).exists()

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if product_exists:
                # Ürün zaten sepette ise, miktarını güncelle
                shop_cart_item = ShopCart.objects.get(product_id=id, user_id=current_user)
                shop_cart_item.quantity += quantity
                shop_cart_item.save()
            else:
                # Yeni ürünü sepette oluştur
                ShopCart.objects.create(user=current_user, product_id=id, quantity=quantity)

            messages.success(request, "Ürün Başarılı Bir Şekilde Sepetenize Eklenmiştir :) ")
            return HttpResponseRedirect(url)

    else:
        if product_exists:
            # Ürün zaten sepette ise, miktarını artır
            shop_cart_item = ShopCart.objects.get(product_id=id, user_id=current_user)
            shop_cart_item.quantity += 1
            shop_cart_item.save()
        else:
            # Yeni ürünü sepette oluştur
            ShopCart.objects.create(user=current_user, product_id=id, quantity=1)

        messages.success(request, "Ürün Başarılı Bir Şekilde Sepetenize Eklenmiştir :) ")
        return HttpResponseRedirect(url)

    messages.warning(request, "Ürün Sepete Eklenemedi :( ")
    return HttpResponseRedirect(url)

@login_required(login_url='/login')
def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart_items = ShopCart.objects.filter(user_id=current_user)
    total = sum(item.product.price * item.quantity for item in shopcart_items)
    context = {
        'shopcart': shopcart_items,
        'category': category,
        'total': total,
        'current_user': current_user,
    }
    return render(request, 'Shopcart_product.html', context)


@login_required(login_url='/login')
def add_to_cart(request, product_id):
    if request.method == 'POST':
        # Alışveriş sepetine ürün eklemek için gerekli işlemleri gerçekleştirin
        return HttpResponse(f"Ürün {product_id} sepete eklendi.")
    else:
        return HttpResponse("Lütfen geçerli bir istek gönderin.")



