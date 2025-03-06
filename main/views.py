from django.shortcuts import render
from .models import Category, Dish


def index(request):
    categories = Category.objects.filter(is_visible=True)

    context = {
        'categories': categories
    }

    return render(request, 'index.html', context=context)
