from django.shortcuts import render
from .models import Category, Dish
from .forms import ReservationForm


def index(request):
    categories = Category.objects.filter(is_visible=True)
    reservation = ReservationForm(request.POST or None)

    context = {
        'categories': categories,
        'reservation': reservation,
    }

    return render(request, 'index.html', context=context)
