from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import *
from .forms import EmailForm

# Create your views here.


def index(request):
    data = Photo.objects.all()

    context = {'data': data, }
    return render(request, 'index.html', context)


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


def subscribe(request):

    form = EmailForm()

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'index.html', {'form': form, 'count': [1, 2, 3, 4, 5]})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Replace 'home' with your desired URL name
            return redirect('index')
        else:
            error_message = "Invalid credentials"
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})


def like(request, pk):
    all = Photo.objects.all()
    data = Photo.objects.get(pk=pk)

    if request.method == 'POST':
        # for i in data:
        #     newlike = int(like)+1

        # like.update(newlike)
        # print(Photo.objects.filter(pk=pk))

        data.like = data.like+1
        data.save()
        print(data.title)
    return redirect('/')
    return render(request, 'index.html', )


def dislike(request, pk):
    all = Photo.objects.all()
    data = Photo.objects.get(pk=pk)

    if request.method == 'POST':
       

        data.dislike = data.dislike+1
        data.save()
        print(data.title)
    return redirect('/')
    return render(request, 'index.html',)
