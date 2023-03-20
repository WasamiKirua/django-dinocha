from django.urls import path, include
from .views import frontpage, shop, myaccount, edit_myaccount

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('myaccount/', myaccount, name='myaccount'),
    path('edit_mcaccount/', edit_myaccount, name='edit_myaccount'),
    path('shop', shop, name='shop'),
    path('accounts/', include('allauth.urls')),
]
