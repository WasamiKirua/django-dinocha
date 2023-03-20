from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models import Category, Product
from django.conf import settings
import os

def frontpage(request):
    return render(request, 'core/frontpage.html')

@login_required
def myaccount(request):
    return render(request, 'core/my_account.html')

@login_required
def edit_myaccount(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        return redirect('myaccount')
    return render(request, 'core/edit_myaccount.html')

def shop(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'core/shop.html', context)
