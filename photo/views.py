from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    data = Photo.objects.all()
    return render(request, 'index.html', {'data': data})


def photos(request):
    data = Photo.objects.filter(tags='photo')

    return render(request, 'photos.html', {'data': data})


def portraits(request):
    data = Photo.objects.filter(tags='portrait')
    return render(request,  'portraits.html', {'data': data})


def artworks(request):
    data = Photo.objects.filter(tags='artwork')
    return render(request,  'artworks.html', {'data': data})


def single(request, pk):
    data = Photo.objects.filter(pk=pk)
    return render(request, 'single.html', {'data': data})
