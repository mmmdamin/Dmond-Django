from django.urls import path

from shop import views

urlpatterns = [
    path('products/', views.products),
    path('products/<int:product_id>', views.product, name="product"),

]
