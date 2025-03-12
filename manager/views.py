from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
# Create your views here.
def index(request):
    return HttpResponse("Manager Page")