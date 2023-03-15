from django.urls import path, include
from .views import frontpage, shop

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop', shop, name='shop'),
    path('accounts/', include('allauth.urls')),
]
