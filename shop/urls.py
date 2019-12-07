from django.urls import path

from shop import views
from shop.views import SigninView

urlpatterns = [
    path('products/', views.products),
    path('products/<int:product_id>', views.product, name="product"),

    path('signin', views.signin),
    path('login', SigninView.as_view()),
    path('signup', views.signup)

]
