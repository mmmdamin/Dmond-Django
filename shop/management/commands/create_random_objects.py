from django.core.management.base import BaseCommand

from shop.models import Product


class Command(BaseCommand):
    help = 'Generates 10000 random objects'

    def handle(self, *args, **options):
        products = []
        for i in range(10000):
            products.append(Product(name="Product{}".format(i), price=i * 100))

        Product.objects.bulk_create(products)
