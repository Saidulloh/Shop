from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', include('django.contrib.auth.urls'), name='login'),
    path('accounts/logout/', include('django.contrib.auth.urls'), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
