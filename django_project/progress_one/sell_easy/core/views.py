from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Store, Category
from django.template.loader import get_template


# Create your views here.

def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products': products, "categories": categories}
    return render(request, 'core/products.html', context)


def product(request, id):
    product = Product.objects.get(id=id)
    related_products = Product.objects.filter(category=product.category)
    return render(request, 'core/detail.html', {'product':product, 'related_products':related_products})


def stores(request):
    stores = Store.objects.all().values()
    


def stores(request, id):
    pass


def store_products(request, id):
    pass


def categories(request):
    pass


def category(request, id):
    pass
