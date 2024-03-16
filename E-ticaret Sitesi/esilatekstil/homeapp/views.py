import json
from pyexpat.errors import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404 , redirect
from django.views import generic
from homeapp.forms import SearchForm, SignupForm
from homeapp.models import Settings
from product.models import Product, Category
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate
from .forms import SignupForm





def index(request):
    # Ana sayfa için gereken verileri al
    settings = Settings.objects.get()
    category = Category.objects.all()
    sliderdata = Product.objects.all()[:4]
    products = Product.objects.all()

    # Ana sayfa şablonuna bağlamak için bir bağlam oluştur
    context = {
        'settings': settings,
        'sliderdata': sliderdata,
        'category': category,
        'products': products,
    }
    return render(request, 'index.html', context)


def products(request):
    # Tüm kategorileri ve ürünleri al
    category = Category.objects.all()  
    products = Product.objects.all()

    
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'products.html', context)


def category_products(request, id, slug):
    # Kategoriyi ve o kategoriye ait ürünleri al
    category = Category.objects.all()
    categorydata = get_object_or_404(Category, pk=id)
    products = Product.objects.filter(category_id=id)

    context = {
        'category': category,
        'categorydata': categorydata,
        'products': products,
        'slug': slug,
    }
    return render(request, 'products.html', context)


def product_detail(request, product_id):
    # Ürünü al
    product = get_object_or_404(Product, id=product_id)
    
    # Ürünün kategorisini al
    product_category = product.category
    
    # Kategori ve alt kategorileri al
    categories = list(product_category.get_descendants(include_self=True))

    context = {
        'product_category': product_category,
        'categories': categories,
        'product': product,
    }

    return render(request, 'product_detail.html', context)


def product_search(request):
    # Arama formunu işle
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all() 
            query = form.cleaned_data['query']  
            products = Product.objects.filter(title__icontains=query)
            context = {
                'query': query,
                'products': products,
            }
            return render(request, 'product_search.html', context)
    else:
        form = SearchForm()
    return render(request, 'product_search.html', {'form': form})


def product_search_auto(request):
    # Otomatik arama işle
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)
        results = []
        for pl in products:
            place_json = {}
            place_json = pl.city + "," + pl.state
            results.append(products)
            data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return redirect(reverse('login')) 



def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı!')
            # Hatalı giriş durumunda kullanıcıya hata mesajı ekleniyor.
            # Daha sonra kullanıcıyı tekrar login sayfasına yönlendiriyoruz.
            return render(request, 'registration/login.html')


    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'registration/login.html', context)



def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Kullanıcının girdiği şifre
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/login')  # Başarı durumunda yönlendirilecek URL
        # Form geçersiz ise veya oturum açma başarısız ise buraya kadar gelinir
    else:
        form = SignupForm()

    category = Category.objects.all()
    context = {'category': category, 'form': form}
    return render(request, 'registration/signup.html', context)



