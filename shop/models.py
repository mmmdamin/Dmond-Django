from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, RegexValidator
from django.db import models


# https://i.pinimg.com/originals/7a/46/4a/7a464a4844318addffa50fa86fae940d.png


class Logged(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(Logged):
    name = models.CharField(verbose_name="اسم", max_length=1000)
    price = models.IntegerField(verbose_name="قیمت", default=0, validators=[MaxValueValidator(1000000000)])

    def __str__(self):
        return "Name: {name} - Price: {price}".format(
            name=self.name,
            price=self.price
        )


class ProductInstance(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


class Cart(Logged):
    user = models.ForeignKey("Member", on_delete=models.PROTECT)

    @property
    def total_products(self):
        return self.purchases.count()

    # @property
    # def total_price(self):
    #     return self.purchases.agg


class Purchase(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, related_name="purchases")
    product_instance = models.ForeignKey(ProductInstance, on_delete=models.PROTECT)


class Invoice(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)


class Member(models.Model):
    post_code = models.CharField(max_length=10, validators=[RegexValidator(r'(0-9){10}')])
    user = models.OneToOneField(User, on_delete=models.PROTECT)
