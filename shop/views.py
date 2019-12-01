from django.shortcuts import render, get_object_or_404

from shop.models import Product


def products(request):
    all_products = Product.active_objects.all()
    return render(request, "all_products.html", {
        "products": all_products
    })


def product(request, product_id):
    product_instance = get_object_or_404(Product, id=product_id)
    return render(request, "product.html", {
        "product": product_instance
    })
