from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView

from shop.forms import SignInForm, SignUpForm
from shop.models import Product


def products(request):
    all_products = Product.active_objects.all()
    return render(request, "all_products.html", {
        "products": all_products
    })


@login_required
def product(request, product_id):
    product_instance = get_object_or_404(Product, id=product_id)
    return render(request, "product.html", {
        "product": product_instance
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
