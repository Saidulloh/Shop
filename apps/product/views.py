from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.db.models import Q

# Create your views here.
def detail_product(request, id):
    product_detail = Product.objects.filter(id=id)
    images = Images.objects.filter(product_id=id)
    
    return render(request, 'include/product_page.html', locals())


def products(request):
    products = Product.objects.all()

    return render(request, 'include/products.html', {'products':products})


def category_detail(request, id):
    tovar_all = Product.objects.filter(category_id = id)
    category = Category.objects.filter(id = id)

    return render(request, 'include/category_page.html', locals())


def check_out(request):
    return render(request, 'include/check_out.html', locals())


def add_tovar(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = AddProductForm()
    return render(request, 'include/add_tovar.html', {'form':form})


def addreview(request):
    product = get_object_or_404(Product)
    reviews = product.review.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.product = product
            new_review.save()
            return redirect('homepage')
    else:
        form = Review()
    return render(request, 'include/product_page.html', locals())