from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('product_detail/<int:id>/', detail_product, name='detail_product'),
    path('products/', products, name='products'),
    path('category_detail/<int:id>/', category_detail, name='category_detail'),
    path('check_out/', check_out, name='check_out'),
    path('add_product/', add_tovar, name='add_tovar')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
