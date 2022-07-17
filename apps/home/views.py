from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from apps.product.models import *
from .models import *

# Create your views here.
def index(request):
    product_all = Product.objects.all()[:3]
    category_all = Category.objects.all()
    return render(request, 'index.html', locals())