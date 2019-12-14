from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import _user_has_perm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView
from django.core.paginator import Paginator
from shop.forms import SignInForm, SignUpForm, ProductForm
from shop.models import Product


def products(request):
    all_products = Product.active_objects.all()
    p = Paginator(all_products, 10)
    page = request.GET.get('page')
    products = p.get_page(page)

    return render(request, "all_products.html", {
        "products": products
    })


def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_form = ProductForm(instance=product)

    return render(request, "product.html", {
        "product": product,
        "form": product_form
    })


@csrf_exempt
def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                return redirect('/')
            form.add_error(None, 'Username and Password dont match')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {
        'form': form,
    })


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                return redirect('/')
            form.add_error(None, 'Username and Password dont match')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {
        'form': form,
    })


class SigninView(FormView):
    template_name = 'signin.html'
    form_class = SignInForm
    success_url = '/'

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            form.add_error(None, 'Username and Password dont match')
        return super().form_valid(form)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    elif request.method == 'GET':
        form = SignUpForm()
    return render(request, 'signup.html', {
        'form': form,
    })
