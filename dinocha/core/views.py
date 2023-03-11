from django.shortcuts import render, redirect
from django.contrib.auth import login
from product.models import Category, Product
from .forms import SignupForm

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form })

def login_old(request):
    return render(request, 'core/login.html')

def shop(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'core/shop.html', context)
