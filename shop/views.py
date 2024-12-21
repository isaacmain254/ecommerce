from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from .recommender import Recommender

def product_list(request, category_slug=None):
    query = request.GET.get('search')
    print(query)
    category = None
    catgories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if query:
        products = products.filter(name__icontains=query)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    context = {'category': category,'categories': catgories, 'products': products,
                   }
    return render(request, 'shop/product/list.html', context)
                  


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)

    return render(request,
                   'shop/product/detail.html',
                     {'product': product,
                       'cart_product_form': cart_product_form,
                       'recommended_products': recommended_products})