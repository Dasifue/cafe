from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from .models import Product, Category, Cart

User = get_user_model()

def navbar_data():
    categories = Category.objects.all()
    return {"categories":categories}

def all_products(request):
    burgers = Product.objects.filter(category_id=1)
    drinks = Product.objects.filter(category_id=2)
    return render(request, 'all_products.html', {'burgers':burgers, 'drinks':drinks, 'navbar':navbar_data()})

def products_filter(request, category_id):
    products = Product.objects.filter(category = category_id)
    return render(request, 'products_filter.html', {'products':products, 'navbar':navbar_data()})

def saveorder(request): 
    owner = 'henry'
    products = Product.objects.get(id = request.POST['product_id'])
    if request.POST['count'] == False:
        request.POST['count'] = 0
        total_price = int(request.POST['count']) * int(float(products.price))
        cart = Cart.objects.create(
            owner=owner,
            total_price=total_price,
            products=products
        )
    cart.save()
    return redirect('shop:all_products')
