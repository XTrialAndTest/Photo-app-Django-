from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # all photos of one kind
    path('photos', views.photos, name='photos'),
    path('portraits', views.portraits, name='portraits'),
    path('artworks', views.artworks, name='artworks'),

    # single page photo
    path('single/<str:pk>', views.single, name='single'),







]
