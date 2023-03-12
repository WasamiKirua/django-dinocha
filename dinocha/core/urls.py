from django.urls import path, include
from .views import frontpage

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('accounts/', include('allauth.urls')),
]
