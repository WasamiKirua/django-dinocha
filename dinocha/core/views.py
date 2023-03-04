from django.shortcuts import render
from product.models import Category, Product

def frontpage(request):
    return render(request, 'core/frontpage.html')

def shop(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'core/shop.html', context)
