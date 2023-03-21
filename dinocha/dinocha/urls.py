from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from product.views import product

urlpatterns = [
    #path('', frontpage, name='frontpage'),
    path('', include('core.urls')),
    path('product/<slug:slug>/', product, name='product'),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
